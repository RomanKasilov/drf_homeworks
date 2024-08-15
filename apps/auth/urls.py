from django.urls import path

from apps.auth.views import ActivUser, RecoveryPasswordEmailView, RecoveryPasswordSetView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivUser.as_view()),
    path('/recovery', RecoveryPasswordEmailView.as_view()),
    path('/recovery/<str:token>', RecoveryPasswordSetView.as_view(),)
]
