from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'carousel', views.CarouselItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('settings/', views.get_site_settings, name='site-settings'),
    path('whatsapp-link/<int:product_id>/', views.get_whatsapp_link, name='whatsapp-link'),
] 