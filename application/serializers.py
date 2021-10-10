from django.contrib.auth.hashers import make_password
from rest_framework import serializers, validators
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'full_name', 'email', 'password')
    
    username = serializers.CharField(read_only=True, label="Логін")
    full_name = serializers.CharField(max_length=50, required=True, label="Повне ім'я")
    email = serializers.EmailField(max_length=100, required=True, label="Email", validators=[validators.UniqueValidator(queryset=CustomUser.objects.all(), message="User with this email already exists!")])
    password = serializers.CharField(max_length=100, min_length=6, required=True, label="Пароль")
    
    def create(self, validated_data):
        username = 'user' + str(CustomUser.objects.order_by('-id').first().id + 1)
        password = make_password(validated_data.pop('password'))
        user = CustomUser.objects.create_user(username=username, password=password, **validated_data)
        return user
    

class MeetingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Meeting
        fields = ('id', 'key', 'start_time', 'end_time')
        
    key = serializers.CharField(read_only=True, label="Ключ", validators=[validators.UniqueValidator(queryset=Meeting.objects.all(), message="Meeteing with this key already exists!")])
    start_time = serializers.DateTimeField(format='%d %B %Y %H:%M:%S', required=True, label="Початок")
    end_time = serializers.DateTimeField(format='%d %B %Y %H:%M:%S', required=True, label="Завершення")


class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        fields = ('id', 'name', 'location', 'number_of_places', 'meetings')
    
    name = serializers.CharField(max_length=50, required=True, label="Назва", validators=[validators.UniqueValidator(queryset=Room.objects.all(), message="Room with this name already exists!")])
    location = serializers.CharField(max_length=256, required=False, label="Місце розташування")
    number_of_places = serializers.IntegerField(max_value=100, min_value=1, required=True, label="Кількість місць")
    meetings = MeetingSerializer(many=True, required=False, read_only=True, label="Бронювання")
    