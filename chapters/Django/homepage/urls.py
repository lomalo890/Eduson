from django.urls import path
from homepage.models import HomeView

urlpatterns = [
    path('', HomeView.as_view())
]


