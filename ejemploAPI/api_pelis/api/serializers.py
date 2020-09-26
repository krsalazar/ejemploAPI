from .models import Pelicula, PeliculaFavorita
from rest_framework import serializers

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
#Serializa todos los campos, pero le podemos indicar que campos son los que necesitamos
        fields = '__all__'

class PeliculaFavoritaSerializer(serializers.ModelSerializer):
    pelicula = PeliculaSerializer()

    class Meta:
        model = PeliculaFavorita
        fields = ['pelicula']