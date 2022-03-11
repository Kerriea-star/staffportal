from rest_framework import generics
from .models import Detail
from .permissions import IsStaffOrReadOnly
from .serializers import DetailSerializer

class StaffList(generics.ListCreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer