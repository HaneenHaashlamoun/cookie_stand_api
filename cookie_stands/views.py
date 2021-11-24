from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Thing
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer


class CookieStandList(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = CookieStandSerializer
