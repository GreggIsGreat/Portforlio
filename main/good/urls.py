from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('userform/', views.userform, name='userform'),
    path('updatepage/<str:pk>/', views.updatepage, name='updatepage'),
    path('currentusers/<str:pk>/', views.currentusers, name='currentusers'),
    path('users/', views.users, name='users'),
    path('stylepage/', views.stylepage, name="stylepage"),
]