from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework import pagination

from crehana.gestion.models import Inscription,VideoProgress
from crehana.gestion.serializers import InscriptionSerializer,VideoProgressSerializer

class Pagination(pagination.PageNumberPagination):       
       page_size = 5

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer
    authentication_classes = [SessionAuthentication,
        BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class=Pagination

class VideoProgressViewSet(viewsets.ModelViewSet):
    queryset = VideoProgress.objects.all()
    serializer_class = VideoProgressSerializer
    authentication_classes = [SessionAuthentication,
        BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class=Pagination