
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from app.viewsets import PontoTuristicoViewSet
from atracoes.viewsets import AtracaoViewSet
from avaliacoes.viewsets import AvaliacaoViewSet
from enderecos.viewsets import EnderecoViewSet
from comentarios.viewsets import ComentarioViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
