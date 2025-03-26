from unittest.mock import patch, MagicMock
from django.core.management import call_command
from django.test import SimpleTestCase
from psycopg2 import OperationalError  # correct error


@patch('core.management.commands.wait_for_db.connect')
class CommandTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_connect):
        """Test waiting for db when db is available immediately."""
        mock_conn = MagicMock()
        patched_connect.return_value = mock_conn

        call_command('wait_for_db')

        self.assertTrue(patched_connect.called)
        mock_conn.close.assert_called_once()

    @patch('core.management.commands.wait_for_db.time.sleep', return_value=True)
    def test_wait_for_db_delay(self, patched_sleep, patched_connect):
        """Test waiting for db with delay when getting OperationalError."""
        # Fail 5 times, then succeed
        mock_conn = MagicMock()
        patched_connect.side_effect = [OperationalError] * 5 + [mock_conn]

        call_command('wait_for_db')

        self.assertEqual(patched_connect.call_count, 6)
        self.assertEqual(patched_sleep.call_count, 5)
        mock_conn.close.assert_called_once()
