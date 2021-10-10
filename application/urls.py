from django.urls import path
from .views import *


urlpatterns = [
    path('', CustomUserAPIView.as_view(), name='base_view'),
    path('users/', CustomUserAPIView.as_view(), name='custom_user_api_view'),
    path('users/create', CustomUserCreateAPIView.as_view(), name='custom_user_create_api_view'),
    path('users/<int:id>/', CustomUserDetailAPIView.as_view(), name='custom_user_detail_api_view'),
    path('rooms/', RoomAPIView.as_view(), name='room_api_view'),
    path('rooms/create', RoomCreateAPIView.as_view(), name='room_create_api_view'),
    path('rooms/<int:id>/', RoomDetailAPIView.as_view(), name='room_detail_api_view'),
    path('rooms/<int:id>/meetings/', RoomMeetingsAPIView.as_view(), name='room_meetings_api_view'),
    path('rooms/<int:id>/meetings/create', MeetingCreateAPIView.as_view(), name='meeting_create_api_view'),
]
