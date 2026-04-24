from rest_framework.viewsets import ModelViewSet
from .seralizers import CategorySeralizer,ProductSeralizer,DaraxtSeralizer
from .models import Category,Product,Daraxt

# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizer
    

    

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer


class DaraxtViewSet(ModelViewSet):
    queryset = Daraxt.objects.all()
    serializer_class = DaraxtSeralizer