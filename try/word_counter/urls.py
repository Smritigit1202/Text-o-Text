# word_counter/urls.py
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.counter, name='word_counter'),  # Map the view to the root URL
]
