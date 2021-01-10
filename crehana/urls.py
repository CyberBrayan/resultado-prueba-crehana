from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from crehana.events.views import EventAPIView
from crehana.curso.views import CategoryViewSet,CourseViewSet
from crehana.gestion.views import InscriptionViewSet,VideoProgressViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoryViewSet)
router.register(r'cursos', CourseViewSet)
router.register(r'inscripciones', InscriptionViewSet)
router.register(r'progreso_video', VideoProgressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'auths/',ObtainAuthToken.as_view()),
    path('', include(router.urls)),
    path('create_event/',EventAPIView.as_view()), 
]
