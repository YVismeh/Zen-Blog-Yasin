from django.urls import path
from .views import HomeView, AboutView, contact_us

app_name = "root"
urlpatterns = [
path('', HomeView.as_view(), name="home"),
path('about', AboutView.as_view(), name="about"),
path('contact', contact_us, name="contact"),
]