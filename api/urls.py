from django.urls import include, path
from rest_framework import routers
from .views import *
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title='Library Catelog Project')

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet,basename='categories')
router.register(r'author', AuthorViewSet,basename='author')
router.register(r'covers', CoverViewSet,basename='cover')
router.register(r'publisher', PublisherViewSet,basename='publishers')
router.register(r'booksinfo', BookInfoViewSet,basename='books')
router.register(r'books/autocomplete', BookAutocompleteViewSet, basename='book-autocomplete')
router.register(r'related-books/(?P<category_id>\d+)', RelatedBooksViewSet, basename='related-books')

urlpatterns = [
    path('', include(router.urls)),
]