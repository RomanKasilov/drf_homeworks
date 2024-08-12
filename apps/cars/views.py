from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.permissions.is_superuser_permission import IsSuperUser

from apps.cars.filter import CarFilter
# from apps.cars.filter import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


class CarListAPIView(ListAPIView):
    serializer_class = CarSerializer
    # pagination_class = PageNumberPagination
    queryset = CarModel.objects.less_than_year(2024)
    filterset_class = CarFilter
    permission_classes = (AllowAny,)

    # def get_queryset(self):
    #     print(self.request.user.profile.name)
    #     return super().get_queryset()

    # def get_queryset(self):
    #     return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)


class CarAddPhotoView(UpdateAPIView):
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)

