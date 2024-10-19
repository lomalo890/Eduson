from django.db import models
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

# Create your models here.

class HomeView(TemplateView):
    template_name = 'homepage.html'







