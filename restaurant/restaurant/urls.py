from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('meal.urls') ), # home and show item
    path('about_us/',include('about_us.urls') ),
]
