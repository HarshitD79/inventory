from django.shortcuts import render
# views.py — Handles API Logic (CRUD, Search, Filter)
from rest_framework import viewsets
from .models import Category, Product, Supplier, StockIn, StockOut
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    SupplierSerializer,
    StockInSerializer,
    StockOutSerializer
)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination  


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')  
    serializer_class = CategorySerializer

    # Enable filtering, searching, sorting
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    pagination_class = CustomPagination



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'name']
    search_fields = ['name', 'category__name']  
    ordering_fields = ['name', 'price', 'quantity_in_stock']
    pagination_class = CustomPagination


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = SupplierSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'contact']
    ordering_fields = ['name']
    pagination_class = CustomPagination



class StockInViewSet(viewsets.ModelViewSet):
    queryset = StockIn.objects.all().order_by('-date')  # recent first
    serializer_class = StockInSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['product', 'supplier', 'date']
    search_fields = ['product__name', 'supplier__name']
    ordering_fields = ['date', 'quantity']
    pagination_class = CustomPagination


class StockOutViewSet(viewsets.ModelViewSet):
    queryset = StockOut.objects.all().order_by('-date')
    serializer_class = StockOutSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['product', 'issued_to', 'date']
    search_fields = ['product__name', 'issued_to']
    ordering_fields = ['date', 'quantity']
    pagination_class = CustomPagination





