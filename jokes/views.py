from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from .models import Joke
from .forms import JokeForm

# Create your views here.
class JokeCreateView(CreateView):
    model = Joke
    # fields = ['question', 'answer']  now uses ModelForm
    form_class = JokeForm

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')
    
class JokeDetailView(DetailView):
    model = Joke
    
class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    # fields = ['question', 'answer']  now uses ModelView
    form_class = JokeForm
