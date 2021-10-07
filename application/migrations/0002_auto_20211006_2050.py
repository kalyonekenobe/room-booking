# Generated by Django 3.2.8 on 2021-10-06 17:50

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(unique=True, verbose_name='Ключ зустрічі')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата та час початку')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата та час завершення')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Назва')),
                ('location', models.CharField(blank=True, max_length=256, verbose_name='Розташування')),
                ('number_of_places', models.PositiveSmallIntegerField(default=1, verbose_name='Кількість місць')),
                ('meetings', models.ManyToManyField(related_name='room_meetings', to='application.Meeting', verbose_name='Зустрічі')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='members',
            field=models.ManyToManyField(related_name='meeting_members', to=settings.AUTH_USER_MODEL, verbose_name='Користувачі'),
        ),
    ]
