
# Importar o AVG para calcular a média das avaliações
from django.db.models import Avg


from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from genres.models import Genre
from actors.models import Actor


class MovieModelSerializer(serializers.ModelSerializer):
    # calcular a média das avaliações 
    
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
        
    # função para calcular a média das avaliações, vem do ORM do Django
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return rate
        return None
    
    # validar datas antes de salvar ou atualizar
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("A data nao pode ser anterior a 1900.")
        return value

    # Validar número de caracteres do resumo
    def validate_resume(self, value):
        if len(value) < 500:
            raise serializers.ValidationError("O resumo deve ser maior que 200 caracteres.")
        return value
    

class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
    
