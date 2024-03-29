
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    # /music/99/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/99/update/
    path('album/<int:pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/99/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    # /music/register/
    path('register/', views.UserFormView.as_view(), name='register'),
]
