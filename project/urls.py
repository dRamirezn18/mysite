from django.urls import path
from .views import index

urlpatterns = [
  path("<str:pk>", index, name="index"),
]