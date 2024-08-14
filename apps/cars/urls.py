from django.urls import path

from apps.cars.views import CarAddPhotoView, CarListAPIView, CarRetrieveUpdateDestroyAPIView, TestEmailView

urlpatterns = [
    path('', CarListAPIView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyAPIView.as_view()),
    path('/<int:pk>/photo', CarAddPhotoView.as_view()),
    path('/test', TestEmailView.as_view())

]
