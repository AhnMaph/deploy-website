from rest_framework import serializers
from .models import Novel
from genres.serializers import GenresSerializer
class NovelSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True, read_only=True)
    class Meta:
        model = Novel
        fields = '__all__'
        read_only_fields = ['numViews', 'numFavorites','numChapters', 'numLikes', 'numComments']
