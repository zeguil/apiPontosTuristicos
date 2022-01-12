from rest_framework.viewsets import ModelViewSet
from .models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filterset_fields = ("nome", 'descricao')