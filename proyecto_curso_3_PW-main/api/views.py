from rest_framework import viewsets
from rest_framework.response import Response
from .serial import FutbolistaSerializer
from .models import Futbolista

# Create your views here.

class FutbolistaViewSet(viewsets.ModelViewSet):
    

    queryset = Futbolista.objects.all().order_by('id')
    serializer_class = FutbolistaSerializer


