from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^invite/$', views.invite_member, name='invite'),
    #url(r'^activate/<uuid:token>/$',
       # views.activate_membership, name='member-register'),
    url(r'^validate/(?P<uidb64>[0-9A-Za-z_\-]+)/$',
    views.activate_membership,
    name='member-register')
]