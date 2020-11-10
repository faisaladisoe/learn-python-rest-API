from studentapi.viewsets import BiodataViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('biodata', BiodataViewset)