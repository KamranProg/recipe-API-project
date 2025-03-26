from unittest.mock import patch, MagicMock
from django.core.management import call_command
from django.test import SimpleTestCase
from psycopg2 import OperationalError


class CommandTests(SimpleTestCase):
    @patch("psycopg2.connect")
    def test_wait_for_db_ready(self, mock_connect):
        """Test waiting for db when db is available immediately."""
        call_command("wait_for_db")
        self.assertTrue(mock_connect.called)

    @patch("time.sleep", return_value=None)
    @patch("psycopg2.connect")
    def test_wait_for_db_delay(self, mock_connect, mock_sleep):
        """Test waiting for db with delay when getting OperationalError."""
        mock_connect.side_effect = [OperationalError] * 5 + [MagicMock()]
        call_command("wait_for_db")
        self.assertEqual(mock_connect.call_count, 6)
