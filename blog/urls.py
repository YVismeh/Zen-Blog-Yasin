from django.urls import path
from .views import BlogView, BlogDetailsView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name="blogs"),
    path('category/<str:category>', BlogView.as_view(), name="category"),
    path('details/<int:pk>',BlogDetailsView.as_view(), name="blog-details"),
]
