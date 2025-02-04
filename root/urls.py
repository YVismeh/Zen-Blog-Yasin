from django.urls import path
from .views import HomeView, AboutView

app_name = "root"
urlpatterns = [
path('', HomeView.as_view(), name="home"),
path('about', HomeView.as_view(), name="home"),
path('contact', HomeView.as_view(), name="home"),
]