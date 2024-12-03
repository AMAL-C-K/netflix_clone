from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile_list', views.profile_list, name='profile_list'),
    path('profile_create', views.profile_create, name='profile_create'),
    path('movie_list/<str:profile_id>', views.movie_list, name='movie_list'),
    path('movie_detail/<str:movie_id>', views.movie_detail, name='movie_detail'),
    path('play-movie/<str:movie_id>', views.movieplay, name='play-movie'),
]