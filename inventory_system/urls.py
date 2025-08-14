
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls), 

     #Yeh app ke URLs ko include karta hai
    path('api/', include('inventory.urls')),
]
