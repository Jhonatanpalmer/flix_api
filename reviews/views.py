#from django.shortcuts import render


### Importar modulos necessários ###
from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  # Defina o serializer apropriado aqui


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  # Defina o serializer apropriado aqui
    
    