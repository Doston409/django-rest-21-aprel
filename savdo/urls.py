from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,ProductViewSet,CustomerViewSet,OrderViewSet,SupplierViewSet


router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'supplier', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]