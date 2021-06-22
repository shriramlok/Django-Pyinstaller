from django.urls import path
from . import views

urlpatterns = [
    path('resnet/',views.resnet_predict, name = 'pred'),
]