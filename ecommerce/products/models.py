from django.db import models

# Create your models here.
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload="categories")
