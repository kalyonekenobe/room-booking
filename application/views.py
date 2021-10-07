from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.http import HttpRequest, HttpResponse


class BaseView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'rooms': Room.objects.all(),
        }
        return render(request, 'base.html', context)
