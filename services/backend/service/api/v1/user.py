from django.urls import path
from apps.user import views


urlpatterns = [
    path('', views.LoginAPIView.as_view()),
    path('register/', views.RegistrationAPIView.as_view()),
    path('rents/', views.UserRentsAPIView.as_view()),
    path('search/<str:username>/', views.FindUserAPIView.as_view()),
    path('search/<str:username>/rents/', views.UserRentsAPIView.as_view()),
]
