
from django.urls import path
from .views import BlogListview, BlogDetailview

urlpatterns = [
    path('', BlogListview.as_view(), name="home"),
    path('<slug:slug>/', BlogDetailview.as_view(), name="post_detail")
]
