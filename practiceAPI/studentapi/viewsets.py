from rest_framework import viewsets
from . import models, serializers

class BiodataViewset(viewsets.ModelViewSet):
    queryset = models.Biodata.objects.all()
    serializer_class = serializers.BiodataSerializer