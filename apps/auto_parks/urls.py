from django.urls import path

from apps.auto_parks.views import AutoParksAddCarView, AutoParksListCreateView

urlpatterns = [
    path('', AutoParksListCreateView.as_view()),
    path('/<int:pk>/cars', AutoParksAddCarView.as_view())
]
