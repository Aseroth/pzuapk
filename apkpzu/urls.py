from django.urls import path
from . import views

urlpatterns = [
    path('', views.apk_list, name='apk_list'),
]