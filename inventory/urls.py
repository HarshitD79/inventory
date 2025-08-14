
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ProductViewSet,
    SupplierViewSet,
    StockInViewSet,
    StockOutViewSet
)

# DRF ka router (yeh automatically CRUD endpoints banata hai)
router = DefaultRouter()

# har ViewSet ko URL path ke sath register kar rahe hain
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('suppliers', SupplierViewSet)
router.register('stock-in', StockInViewSet)
router.register('stock-out', StockOutViewSet)

# Final URL patterns jisse DRF endpoints activate hote hain
urlpatterns = [
    path('', include(router.urls)),
]