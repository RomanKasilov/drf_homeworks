from django.urls import path

from apps.cars.views import CarListAPIView, CarRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CarListAPIView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyAPIView.as_view()),

]
