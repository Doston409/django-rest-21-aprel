from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewSet, WaiterViewSet, TableViewSet

router = DefaultRouter()
router.register(r'dish', DishViewSet)
router.register(r'waiter', WaiterViewSet)
router.register(r'table', TableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]