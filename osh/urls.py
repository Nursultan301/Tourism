from django.urls import path

from osh.views import PostListView, PostDetailView, TripsListview, TripsDetailView, FoodListView

urlpatterns = [
    path('', PostListView.as_view(), name='post'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('trips-detail/<int:pk>/', TripsDetailView.as_view(), name='trips_detail'),
    path('trips/', TripsListview.as_view(), name='trips'),
    path('food/', FoodListView.as_view(), name='food'),

]
