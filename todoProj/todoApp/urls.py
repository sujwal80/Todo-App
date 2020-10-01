from django.urls import path
from .views import home, update, delete

urlpatterns = [
    path('', home, name="home"),
    path('update/<str:pk>', update, name="update_url"),
    path('delete/<str:pk>', delete, name="delete_url")
]