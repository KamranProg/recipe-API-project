import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client


@pytest.mark.django_db
class TestAdminUserManagement:

    def setup_method(self):
        """Create superuser, normal user, and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="adminpass"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="userpass",
            first_name="Test",
            last_name="User"
        )

    def test_users_list(self):
        """Test that users are listed in the Django admin user list page"""
        url = reverse("admin:accounts_user_changelist")
        response = self.client.get(url)

        assert response.status_code == 200
        assert self.user.email in response.content.decode()
        assert self.user.first_name in response.content.decode()
        assert self.user.last_name in response.content.decode()

    def test_edit_user_page(self):
        """Test that the user edit page works"""
        url = reverse("admin:accounts_user_change", args=[self.user.id])
        response = self.client.get(url)

        assert response.status_code == 200
        assert "Change user" in response.content.decode()
