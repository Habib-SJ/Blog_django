
from django.urls import path
from .views import BlogListview, BlogDetailview

urlpatterns = [
    path('', BlogListview),
    path('<int:pk>', BlogDetailview)
]
