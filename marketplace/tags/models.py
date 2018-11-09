from django.db import models
from model_utils.models import TimeStampedModel


class Tag(TimeStampedModel):
    """Tag model, name is unique."""

    name = models.CharField(max_length=250, unique=True)
