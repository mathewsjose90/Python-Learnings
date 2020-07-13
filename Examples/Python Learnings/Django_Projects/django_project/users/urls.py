from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.register, name='users-register'),
    path('/', views.profile, name='users-profile'),

]
