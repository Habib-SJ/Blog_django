from django.shortcuts import render
from django.views import generic
from .models import blog_model

# Create your views here.

class BlogListview(generic.ListView):
    queryset = blog_model.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class BlogDetailview(generic.DetailView):
    model = blog_model
    template_name = 'detailpost.html'


