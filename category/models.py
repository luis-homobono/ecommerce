from django.db import models
from django.urls import reverse


class Category(models.Model):
    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    def get_url(self):
        return reverse('products_category', args=[self.slug])

    def __str__(self):
        return self.category_name