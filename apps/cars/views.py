from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from apps.cars.filter import CarFilter
# from apps.cars.filter import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateAPIView(ListCreateAPIView):
    serializer_class = CarSerializer
    # pagination_class = PageNumberPagination
    queryset = CarModel.objects.all()
    filterset_class = CarFilter

    # def get_queryset(self):
    #     return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
