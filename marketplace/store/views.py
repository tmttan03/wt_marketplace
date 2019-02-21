from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.models import User
from django.core.mail import EmailMessage
from django.template import RequestContext

from .tokens import account_activation_token
from .forms import InvitationForm
from .models import StoreInvite


def invite_member(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invite = form.save(commit=False)
            invite.owner = request.user
            invite.save()
            role = form.cleaned_data.get('role')
            current_site = get_current_site(request)
            mail_subject = f'Be one of my { role }'
            to_email = form.cleaned_data.get('invited')
            #import pdb; pdb.set_trace()
            #message = render_to_string('acc_active_email.html', {
                #'invite': invite,
                #'domain': current_site.domain
            #}), 
            
            #email = EmailMessage(
                #mail_subject, message, to=[to_email]
            #)
            #email.send()
            return HttpResponse('Please wait for his/her reply')
    else:
        form = InvitationForm()
    return render(request, 'invite.html', {'form': form})


def activate_membership(request,token):
    invite = get_object_or_404(StoreInvite, token=token)
    
    import pdb; pdb.set_trace()
    if not invite.is_used:
        invite.is_used = True
        invite.save()
        #return redirect('/')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')