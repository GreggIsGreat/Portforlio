from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
    path('reviewform/', views.reviewform, name='reviewform'),
    path('deletereview/<str:pk>/', views.deletereview, name='deletereview'),
]
