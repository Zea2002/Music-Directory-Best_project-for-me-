from django.urls import path
from .views import (
    MusicianListView, MusicianDetailView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView,
    AlbumCreateView, AlbumUpdateView, AlbumDeleteView
)

urlpatterns = [
    path('', MusicianListView.as_view(), name='musician-list'),
    path('musician/<int:pk>/', MusicianDetailView.as_view(), name='musician-detail'),
    path('musician/create/', MusicianCreateView.as_view(), name='musician-create'),
    path('musician/<int:pk>/update/', MusicianUpdateView.as_view(), name='musician-update'),
    path('musician/<int:pk>/delete/', MusicianDeleteView.as_view(), name='musician-delete'),
    path('album/create/', AlbumCreateView.as_view(), name='album-create'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
]
