from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path('mineral/<int:pk>', views.mineral_detail, name='detail'),
    path('', views.home, name='home'),
    path('random', views.random_detail, name='random'),
]
