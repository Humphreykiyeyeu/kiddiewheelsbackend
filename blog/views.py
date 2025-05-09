from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Product, CarouselItem, SiteSettings
from .serializers import ProductSerializer, CarouselItemSerializer, SiteSettingsSerializer

# Create your views here.

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit.
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow admin users to perform write operations
        return request.user and request.user.is_staff

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

class CarouselItemViewSet(viewsets.ModelViewSet):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer
    permission_classes = [IsAdminOrReadOnly]

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_site_settings(request):
    settings = SiteSettings.objects.first()
    if not settings:
        settings = SiteSettings.objects.create(
            whatsapp_number="",
            whatsapp_message_template="Hello, I'm interested in the {product_name} (TSH {price}).\nProduct link: {product_link}"
        )
    serializer = SiteSettingsSerializer(settings)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_whatsapp_link(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        settings = SiteSettings.objects.first()
        
        if not settings:
            return Response({"error": "WhatsApp settings not configured"}, status=400)
            
        message = settings.whatsapp_message_template.format(
            product_name=product.name,
            price=product.price,
            product_link=f"{request.build_absolute_uri('/')[:-1]}/product/{product.id}"
        )
        
        whatsapp_link = f"https://wa.me/{settings.whatsapp_number}?text={message}"
        return Response({"whatsapp_link": whatsapp_link})
        
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
