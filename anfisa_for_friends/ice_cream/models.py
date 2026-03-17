from django.db import models
from core.models import PublishedModel

class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'