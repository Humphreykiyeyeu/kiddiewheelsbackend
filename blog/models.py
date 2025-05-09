from django.db import models
from django.core.validators import URLValidator

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=500)
    category = models.CharField(max_length=100)
    age_range = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=500)
    order = models.IntegerField(default=0)
    primary_button_text = models.CharField(max_length=100, blank=True, null=True)
    primary_button_link = models.URLField(blank=True, null=True)
    secondary_button_text = models.CharField(max_length=100, blank=True, null=True)
    secondary_button_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class SiteSettings(models.Model):
    whatsapp_number = models.CharField(max_length=20)
    whatsapp_message_template = models.TextField(
        default="Hello, I'm interested in the {product_name} (TSH {price}).\nProduct link: {product_link}"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return f"Site Settings - WhatsApp: {self.whatsapp_number}"
