from django.shortcuts import render
from testapp.models import Beer
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class BeerListView(ListView):
    model = Beer
    # default template is beer_list.html
    # default context is beer_list


class BeerDetailView(DetailView):
    model = Beer
    # default template is beer_detail.html
    # default context is beer


class BeerCreateView(CreateView):
    model = Beer
    fields = '__all__'


class BeerUpdateView(UpdateView):
    model = Beer
    fields = ('teast', 'price')


class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('list')
