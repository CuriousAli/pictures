from rest_framework import serializers
from .models import Picture



class PictureAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ["name", "image"]


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'