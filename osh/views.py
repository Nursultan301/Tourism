from django.shortcuts import render
from django.views.generic import ListView, DetailView

from osh.models import Post, Trips, Food


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6
    template_name = "osh/index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "osh/detail.html"


class TripsListview(ListView):
    model = Trips
    context_object_name = 'obj_trips'
    paginate_by = 6
    template_name = "osh/trips.html"


class TripsDetailView(DetailView):
    model = Trips
    template_name = "osh/trips-detail.html"


class FoodListView(ListView):
    model = Food
    context_object_name = 'foods'
    paginate_by = 3
    template_name = "osh/food.html"
