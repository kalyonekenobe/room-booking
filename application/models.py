from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    
    full_name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    email = models.EmailField(unique=True, verbose_name="Email")
    password = models.TextField(max_length=100, verbose_name="Пароль")
    
    def __str__(self):
        return self.full_name
    
    def save(self, **kwargs):
        full_name_is_valid = (len(self.full_name) < 50)
        password_is_valid = (6 <= len(self.password) <= 100)
        user_data_is_valid = (full_name_is_valid and password_is_valid)
        if user_data_is_valid:
            super().save(**kwargs)


class Meeting(models.Model):
    
    key = models.SlugField(unique=True, verbose_name='Ключ зустрічі')
    start_time = models.DateTimeField(default=timezone.now, verbose_name='Дата та час початку')
    end_time = models.DateTimeField(default=timezone.now, verbose_name='Дата та час завершення')
    
    def __str__(self):
        return f"Зустріч №{self.id} ({self.start_time} - {self.end_time})"


class Room(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name="Назва")
    location = models.CharField(max_length=256, blank=True, verbose_name="Розташування")
    number_of_places = models.PositiveSmallIntegerField(default=1, verbose_name="Кількість місць")
    meetings = models.ManyToManyField(Meeting, verbose_name='Зустрічі', related_name='room_meetings')
    
    def __str__(self):
        return self.name
    
    def is_booked(self):
        return True if self.meetings.count() else False
    
    def save(self, **kwargs):
        name_is_valid = (len(self.name) < 50)
        number_of_places_is_valid = (0 < self.number_of_places <= 100)
        room_is_valid = (name_is_valid and number_of_places_is_valid)
        if room_is_valid:
            super().save(**kwargs)
            