from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from plays.models import Show


# Create your models here.

class HomeView(ListView):
    template_name = 'homepage.html'
    model = Show

    def get_queryset(self):
        return Show.objects.active()


