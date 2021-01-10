from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework import pagination

from crehana.curso.models import Category,Course
from crehana.curso.serializers import CategorySerializer,CourseSerializer

class Pagination(pagination.PageNumberPagination):       
       page_size = 5

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication,
        BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class=Pagination

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication,
        BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class=Pagination