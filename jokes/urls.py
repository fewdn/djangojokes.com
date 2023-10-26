from django.urls import path
from .views import JokeListView

app_name = 'jokes'
urlpatterns = [
    path('', JokeListView.as_view(), name='list'),
]