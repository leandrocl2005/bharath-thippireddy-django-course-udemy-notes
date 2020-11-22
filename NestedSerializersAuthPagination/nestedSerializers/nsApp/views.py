from .models import Author, Book
from .serializer import AuthorSerializer, BookSerializer
from rest_framework import generics
# from rest_framework.pagination import LimitOffsetPagination

# Authentication and Permission in local level
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated,
# DjangoModelPermissions

# Custom paginations
# class AuthorPagination(PageNumberPagination):
#    page_size = 2


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # pagination_class = LimitOffsetPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
