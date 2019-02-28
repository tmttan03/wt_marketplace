from django.urls import path
from .views import (
    UserProductsListView,
    PostView,
    MessageView, 
    DeleteView, 
	UpdateView,
    PublishDraftView,
	MarkAvailableView,
	MarkSoldView,
	RestockView, 
    ProfileView,
    DetailView, 
)

from . import views

urlpatterns = [
    path('create/', PostView.as_view(), name='post-create'),
    path('message/', MessageView.as_view(), name='message'),
    path('item/<int:product_id>/', DetailView.as_view(), name='view-post'),
    path('selling/', UserProductsListView.as_view(), name='user-products'),
    path('delete/<int:product_id>/', DeleteView.as_view(), name='delete-post'),
    path('update/<int:product_id>/', UpdateView.as_view(), name='post-update'),
    path('publish/<int:product_id>/', PublishDraftView.as_view(), name='publish-draft'),
    path('available/<int:product_id>/', MarkAvailableView.as_view(), name='mark-available'),
    path('sold/<int:product_id>/', MarkSoldView.as_view(), name='mark-sold'),
    path('restock/<int:product_id>/', RestockView.as_view(), name='restock'),
    #path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
]
