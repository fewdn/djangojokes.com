from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Joke
from .forms import JokeForm

# Create your views here.
class JokeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Joke
    # fields = ['question', 'answer']  now uses ModelForm
    form_class = JokeForm
    success_message = "Joke created."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
class JokeDetailView(DetailView):
    model = Joke
    
class JokeListView(ListView):
    model = Joke

class JokeUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    # fields = ['question', 'answer']  now uses ModelView
    form_class = JokeForm
    success_message = "Joke updated."

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
