from django.contrib import admin
from django.urls import path, include

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
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
]

