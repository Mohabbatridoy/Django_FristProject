from django.urls import path
from app_1 import views

urlpattenrs = [
    path('index/',views.index, name='index'),
]