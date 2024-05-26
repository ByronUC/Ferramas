from .models import *
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):

    categoria = serializers.CharField(source='categoria.categoria', read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria')

    class Meta:
        model = Producto
        fields = '__all__'




