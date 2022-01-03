
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
