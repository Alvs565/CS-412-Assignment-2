# Alvaro Sanchez Faria
# alvs@bu.edu
# restaurant/urls.py: Handles URL requests from the restaurant page and re-directs it accordingly

from django.urls import path
from django.conf import settings
from . import views

#URL Patterns for restaurant:
urlpatterns = [
    path('', views.main, name="main"),
    path('order', views.order, name="order"),
    path('submit',views.submit, name="submit")
]