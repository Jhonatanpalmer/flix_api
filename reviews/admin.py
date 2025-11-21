from django.contrib import admin

#### IMportar o modelo Review ###
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment')
    


