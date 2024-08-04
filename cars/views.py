from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from cars.models import CarModel
from cars.serializers import CarSerializer
from cars.filter import car_filter


class CarListCreateAPIView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
