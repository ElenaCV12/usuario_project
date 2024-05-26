from rest_framework import viewsets
from usuario.models import Usuario
from usuario.api.serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer