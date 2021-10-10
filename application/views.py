import random
from rest_framework.generics import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from application.serializers import *
from application.utils import *


class CustomUserAPIView(ListAPIView):
    serializer_class = CustomUserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()


class RoomAPIView(ListAPIView):
    serializer_class = RoomSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()


class RoomMeetingsAPIView(ListAPIView):
    serializer_class = MeetingSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        room_id = self.kwargs.get('id')
        queryset = queryset.get(id=room_id).meetings.all()
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        if start_time:
            queryset = queryset.filter(end_time__gte=start_time.replace('T', ' ', 1))
        if end_time:
            queryset = queryset.filter(start_time__lte=end_time.replace('T', ' ', 1))
        return queryset


class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()


class RoomDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    lookup_url_kwarg = 'id'
    
    def perform_destroy(self, instance):
        instance.delete()


class CustomUserCreateAPIView(CreateAPIView):
    serializer_class = CustomUserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    
    def perform_create(self, serializer):
        serializer.save()


class CustomUserDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = CustomUserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    lookup_url_kwarg = 'id'
    
    def perform_destroy(self, instance):
        instance.delete()


class MeetingCreateAPIView(CreateAPIView):
    serializer_class = MeetingSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        
        values = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
                  '%', '^', '&', '*', '(', ')', '-', '+', '_', '=')
        key = ""
        for i in range(0, 16):
            index = random.randint(0, len(values) - 1)
            key += values[index]
        key = encode_value(key)
        room = Room.objects.get(id=self.kwargs.get('id'))
        queryset = room.meetings.filter(end_time__gte=serializer.validated_data.get('start_time'),
                                        start_time__lte=serializer.validated_data.get('end_time'))
        if not queryset.count():
            room.meetings.add(serializer.save(key=key))
            room.save()
        else:
            raise serializers.ValidationError("There are some other meetings on selected time range")
