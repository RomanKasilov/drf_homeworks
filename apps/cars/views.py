from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filter import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateAPIView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
