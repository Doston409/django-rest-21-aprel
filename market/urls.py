from .views import CategoryViewSet, ProductViewSet,DaraxtViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include

r = DefaultRouter()
r.register("category", CategoryViewSet)
r.register("product", ProductViewSet)
r.register("daraxt", DaraxtViewSet)


urlpatterns = [
    path("", include(r.urls))
    
]
