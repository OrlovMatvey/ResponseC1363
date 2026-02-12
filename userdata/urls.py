from django.urls import path
from userdata import views

urlpatterns = [
    path('/task', views.user_task),
]
