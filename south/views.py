from django.shortcuts import render
from django.views.generic import ListView, DetailView

from south.models import Osh, Trips, DjalalAbad, Batken


class OshListView(ListView):
    model = Osh
    context_object_name = 'osh'
    paginate_by = 6
    template_name = "south/index.html"


class DjalalAbadListView(ListView):
    model = DjalalAbad
    context_object_name = 'djalalabad'
    paginate_by = 6
    template_name = "south/djalalabad.html"


class BatkenListView(ListView):
    model = Batken
    context_object_name = 'batken'
    paginate_by = 6
    template_name = "south/batken.html"



class PostDetailView(DetailView):
    model = Osh
    template_name = "south/detail.html"


class DjalalabadDetailView(DetailView):
    model = DjalalAbad
    template_name = "south/detail.html"


class BatkenDetailView(DetailView):
    model = Batken
    template_name = "south/detail.html"


class TripsListview(ListView):
    model = Trips
    context_object_name = 'obj_trips'
    paginate_by = 6
    template_name = "south/trips.html"


class TripsDetailView(DetailView):
    model = Trips
    template_name = "south/trips-detail.html"
