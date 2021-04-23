from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from . models import Post
from django.db.models import Q

# Create your views here.

class Inicio(ListView):
    paginate_by = 6
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('-criado')


class Detalhes(DetailView):
    model = Post
    template_name = 'detalhes.html'
    context_object_name = 'post'


class Search(ListView):
    paginate_by = 6
    model = Post
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
                Q(titulo__icontains=query) | Q(sumario__icontains=query)
            )
        return object_list
