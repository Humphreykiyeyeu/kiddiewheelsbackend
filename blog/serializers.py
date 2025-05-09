from rest_framework import serializers
from .models import Product, CarouselItem, SiteSettings

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image','category','age_range','color', 'created_at', 'updated_at', 'featured']

class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = [
            'id',
            'title',
            'description',
            'image',
            'order',
            'primary_button_text',
            'primary_button_link',
            'secondary_button_text',
            'secondary_button_link'
        ]

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['id', 'whatsapp_number', 'whatsapp_message_template'] 