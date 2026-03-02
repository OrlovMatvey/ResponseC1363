from django.urls import path
from taskC import views

urlpatterns = [
    path('', views.get_page),
    path('task', views.user_task),
]
