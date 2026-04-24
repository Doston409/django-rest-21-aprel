from rest_framework.serializers import ModelSerializer
from .models import Category,Product,Daraxt

class CategorySeralizer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSeralizer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class DaraxtSeralizer(ModelSerializer):
    class Meta:
        model = Daraxt
        fields = "__all__"






