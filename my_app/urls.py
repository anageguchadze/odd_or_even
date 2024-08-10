from django.urls import path
from .views import odd_or_even

urlpatterns = [
    path("odd_or_even/<int:num>", odd_or_even),
]