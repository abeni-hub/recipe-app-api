"""
Tests for the recipe app.
"""

from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe
from recipe.serializers import RecipeSerializer


def create_user(**params):
    """Create and return a new user."""
    defaults = {
        'title': 'Sample recipe title',
        'time_minutes': 22,
        'price': Decimal('5.25'),
         'description': 'Sample recipe description.',
          'link': 'http://example.com/recipe.pdf',
    }
    defaults.update(params)

    return get_user_model().objects.create_user(**defaults)
    return recipe
