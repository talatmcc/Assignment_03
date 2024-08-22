from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_item/', views.show_item, name='show_item'),
]
