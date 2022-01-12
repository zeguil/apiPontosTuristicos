from rest_framework.serializers import ModelSerializer
from app.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('nome', 'descricao', 'status', 'foto')