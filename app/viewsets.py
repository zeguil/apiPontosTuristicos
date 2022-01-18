from rest_framework.viewsets import ModelViewSet
from app.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao']
    lookup_field = 'nome'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome_iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao_iexact=descricao)
            
        return queryset

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'status': "Denunciado"})