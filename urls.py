from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('sign/', views.sign, name='sign'),
    path('two/', views.two, name='two'),
]