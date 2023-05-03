from django.urls import path
from apps.rooms import views


urlpatterns = [
    path('', views.ListRoomAPIView.as_view()),
    path('create/', views.CreateRoomAPIView.as_view()),
    path('search/<uuid:pk>/', views.GetRoomAPIView.as_view()),
    path('search/<uuid:pk>/update/', views.UpdateRoomAPIView.as_view()),
    path('search/<uuid:pk>/delete/', views.DestroyRoomAPIView.as_view()),
    path('search/<uuid:pk>/rents/', views.RoomRentsAPIView.as_view()),
]
