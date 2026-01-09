from django.db import models


class BaseModel(models.Model):
    """Base model for future models."""

    class Meta:
        abstract = True

