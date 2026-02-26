"""
Test for models.
"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from core import models

class ModelTests(TestCase):
    """Test models."""

    def setUp(self):
        """Create a superuser for admin tests."""
        self.user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.user)

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [
            ('test1@EXAMPLE.com', 'test1@example.com'),
            ('Test2@EXAMPLE.com', 'Test2@example.com'),
            ('TEST3@EXAMPLE.COM', 'TEST3@example.com'),
            ('test4@example.com', 'test4@example.com'),
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password='sample123',
            )
            self.assertEqual(user.email, expected)

    def test_create_user_without_email_raises_error(self):
        """Test creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='test123',
            )

    def test_create_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_edit_user_page(self):
        """Test editing a user page loads correctly."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


def test_create_user_recipe(self):
    """Test creating a recipe is successful."""
    user = get_user_model().objects.create_user(
        'test@example.com',
        'testpass123',
    )

    recipe = models.Recipe.objects.create(
        user=user,
        title='Sample recipe name',
        time_minutes=5,
        price=Decimal('5.50'),
        description='Sample recipe description.',
    )
    self.assertEqual(str(recipe), recipe.title)