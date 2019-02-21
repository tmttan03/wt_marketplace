from django.urls import path
from .views import PostView

from . import views

urlpatterns = [
    path('create/', PostView.as_view(), name='post-create'),
]
