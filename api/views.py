from rest_framework import viewsets
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import *
from rest_framework.viewsets import ReadOnlyModelViewSet

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CoverViewSet(viewsets.ModelViewSet):
    queryset = CoverImage.objects.all()
    serializer_class = CoverSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BookInfoViewSet(viewsets.ModelViewSet):
    serializer_class = BookInfoSerializer
    def get_queryset(self):
        queryset = BooksInfo.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        else:
            queryset = queryset.all()
        return queryset

class BookAutocompleteViewSet(viewsets.ViewSet):
    def list(self, request):
        search_term = request.query_params.get('search', None)
        if search_term:
            queryset = BooksInfo.objects.filter(
                Q(english_name__icontains=search_term)|
                Q(bangla_name__icontains=search_term)
            )
        else:
            queryset = BooksInfo.objects.all()

        serializer = BookSearchSerializer(queryset, many=True)
        return Response(serializer.data)
    
class RelatedBooksViewSet(ReadOnlyModelViewSet):
    serializer_class = BookInfoSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return BooksInfo.objects.none()

        return BooksInfo.objects.filter(category=category)