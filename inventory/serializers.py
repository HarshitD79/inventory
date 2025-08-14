from rest_framework import serializers
from .models import Category, Product, Supplier, StockIn, StockOut

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  #include all fields (id, name, description)



class ProductSerializer(serializers.ModelSerializer):
    category_name = CategorySerializer(source='category', read_only=True)  # show full category JSON

    class Meta:
        model = Product
        fields = '__all__'  #includes id, name, category, price, etc.



class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'




class StockInSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)
    supplier_detail = SupplierSerializer(source='supplier', read_only=True)

    class Meta:
        model = StockIn
        fields = '__all__'




class StockOutSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = StockOut
        fields = '__all__'

