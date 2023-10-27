from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Joke

# Create your views here.
class JokeDetailView(DetailView):
    model = Joke
    
class JokeListView(ListView):
    model = Joke

