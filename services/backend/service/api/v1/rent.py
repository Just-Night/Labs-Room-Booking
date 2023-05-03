from django.urls import path
from apps.rooms import views


urlpatterns = [
    path('', views.RentCreateAPIView.as_view()),
    path('<uuid:room>/', views.RentDetailAPIView.as_view()),
]
