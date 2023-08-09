from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('greet/<str:username>/', views.greet_user_view, name='greet'),
    path('farewell/<str:username>/', views.farewell_user_view, name='farewell'),
]
