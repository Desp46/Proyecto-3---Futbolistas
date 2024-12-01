from rest_framework import serializers

from .models import Futbolista

class FutbolistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Futbolista
        fields = ['id','nombres','apellidos','club','fecha_contrato','salario']