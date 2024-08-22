from django.urls import path, include
from . import views

urlpatterns = [
    path('app_2/',views.index),
    path('',views.base),
    path('show_items/',views.show_items),
]