import pytest
from accounts.models import User


@pytest.mark.django_db
class TestUserModel:

    def test_create_user_with_email_successful(self) -> None:
        """
        test_create_user_with_email_successful |
        Test creating a new user with an email is successful
        """
        email = "test@example.com"
        password = "testpass123"
        user = User.objects.create_user(
            email=email,
            password=password,
        )

        assert user.email == email
        assert user.check_password(password)

    def test_new_user_email_normalized(self) -> None:
        """
        test_new_user_email_normalized |
        Test email is normalized for new users
        """
        sample_emails = [
            ["test1@EXAMPLE.COM", "test1@example.com"],
            ["Test2@Example.COM", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = User.objects.create_user(email=email, password="test123")
            assert user.email == expected

    def test_new_user_without_email_raises_error(self) -> None:
        """
        test_new_user_without_email_raises_error |
        Test creating a user without an email raises a ValueError
        """
        with pytest.raises(ValueError):
            User.objects.create_user(email=None, password="test123")

    def test_create_superuser(self) -> None:
        """
        test_create_superuser |
        Test creating a new superuser
        """
        email = "superuser@example.com"
        password = "superpass123"
        user = User.objects.create_superuser(email=email, password=password)

        assert user.is_superuser is True
        assert user.is_staff is True
        assert user.email == email
        assert user.check_password(password)
