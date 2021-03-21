from django.urls import path

from . import views

urlpatterns = [
    path('', views.FeedItemListView.as_view(), name='home')
]
