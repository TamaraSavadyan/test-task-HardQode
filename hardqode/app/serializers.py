from rest_framework import serializers
from app.models import LessonView, Product

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ('lesson', 'viewed', 'view_time_seconds')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'owner')

