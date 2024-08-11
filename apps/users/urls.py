from django.urls import path

from apps.users.views import UserAdminDelView, UserAdminPassView, UserBlockView, UserListCreateView, UserUnBlockView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
    path('/<int:pk>/admin_pass', UserAdminPassView.as_view()),
    path('/<int:pk>/admin_del', UserAdminDelView.as_view()),

]
