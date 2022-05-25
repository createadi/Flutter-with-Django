from django.urls import path
from core import views

urlpatterns = [
    path('demo/', views.DemoList),
]