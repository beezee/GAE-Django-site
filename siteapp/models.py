from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=30, validators=[RegexValidator(r'^[a-zA-Z0-9\_\-]+$', 'Slugs can only contain letters, numbers, hyphens and underscores')])
    content = models.TextField()