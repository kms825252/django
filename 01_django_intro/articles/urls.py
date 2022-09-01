from django.urls import path
from articles import views

urlpatterns = [
    path('index/', views.index),
    path('greegin/', views.greeting),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<name>/', views.hello),
]