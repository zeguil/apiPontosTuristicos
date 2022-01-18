from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecoSerializer
from .models import Endereco
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)