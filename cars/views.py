from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from cars.models import CarModel
from cars.serializers import CarSerializer


class CarListCreateAPIView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
