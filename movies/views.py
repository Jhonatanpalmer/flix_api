from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieStatsSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from reviews.models import Review

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer   
    

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer 
    
    
class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    
    
    def get (self, request):
        total_movies = self.queryset.count()
        
        ### mostrar os filmes de genre, e faz um contador mostrando quantos filmes tem em cada genre
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))  
        
        ### Total de reviews na plataforma
        total_reviews = Review.objects.count()    
        
        ### media de estrelas
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']     
        
           
        data={
                "total_movies": total_movies,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                ### mostrar apenas uma casa decimal, e o if caso nao tenha reviews, retornar 0
                "average_stars": round(average_stars, 1) if average_stars is not None else 0,}
        
        
        ### Retornar os dados para o usuario
        
        serializers = MovieStatsSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        return response.Response(data=serializers.validated_data, status=status.HTTP_200_OK,)
    
    
    