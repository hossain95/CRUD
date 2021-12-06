from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<str:pk>/', views.detail, name="detail"),
    path('create_view/', views.create_view, name="create_view"),
    path('list_view/', views.list_view, name="list_view"),
    path('<id>/', views.details_view),
    path('', views.update_view),
]