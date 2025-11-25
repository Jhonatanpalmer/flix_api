from django.contrib import admin
from django.urls import path

### Importar a view do app genres, genre_view é o nome da view
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

### Importar as views do app actors
from actors.views import ActorCreateView, ActorRetrieveUpdateDestroyView

###Importar as views do app movies
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView

### Importar as views do app reviews ###
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    ### Criar URL para o app genres
    
    
    ### Criar URL para listar e criar generos
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    
   
    #### URLS de Actors
    path('actors/', ActorCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
    
    
    #### URLS de Movies
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    
    
    #### URLS de Reviews
    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
    
    
]

