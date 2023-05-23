from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverImage
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksInfo
        fields = '__all__'


class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksInfo
        fields = '__all__'
