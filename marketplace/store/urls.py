from django.conf.urls import url
from .views import (
	SendInvitation,
	ActivationLink
)
from . import views
urlpatterns = [
    url(r'^invite/$', SendInvitation.as_view(), name='invite'),
    #url(r'^activate/<uuid:token>',
        #ActivationLink.as_view(), name='member-register'),
    url(r'^validate/(?P<uidb64>[0-9A-Za-z_\-]+)/$',
    ActivationLink.as_view(),
    name='member-register')
]