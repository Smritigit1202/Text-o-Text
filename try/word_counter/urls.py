# word_counter/urls.py
from django.urls import path
from . import views  # Import views from the current app
from .views import find_replace_view
from .views import ana_view 

urlpatterns = [
    path('', views.counter, name='word_counter'),  # Map the view to the root URL
    path('find-replace/', find_replace_view, name='find_replace'),
     path('ana/', ana_view, name='ana'),
]
