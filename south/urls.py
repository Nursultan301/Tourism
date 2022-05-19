from django.urls import path

from south.views import OshListView, PostDetailView, TripsListview, TripsDetailView, DjalalabadDetailView, \
    BatkenDetailView, DjalalAbadListView, BatkenListView

urlpatterns = [
    path('', OshListView.as_view(), name='osh'),
    path('djalalabad/', DjalalAbadListView.as_view(), name='djalalabad'),
    path('batken/', BatkenListView.as_view(), name='batken'),

    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('dj/detail/<int:pk>/', DjalalabadDetailView.as_view(), name='dj-detail'),
    path('ba/detail/<int:pk>/', BatkenDetailView.as_view(), name='ba-detail'),
    path('trips-detail/<int:pk>/', TripsDetailView.as_view(), name='trips_detail'),
    path('trips/', TripsListview.as_view(), name='trips'),

]
