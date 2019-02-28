import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from accounts.models import User


from .forms import InvitationForm, RegisterWithRoleForm
from .models import Store, StoreInvite, StoreMembers


class SendInvitation(LoginRequiredMixin, TemplateView):
    """Send Invitation Link for Potential Store Members"""
    template_name = 'invite.html'
    form = InvitationForm

    def get(self,*args,**kwargs):
        store = get_object_or_404(Store, owner=self.request.user)
        context = super(SendInvitation, self).get_context_data(**kwargs)
        context['form'] = self.form()
        context['members'] = StoreMembers.objects.filter(store=store)
        return render(self.request, self.template_name, context)
        
    def post(self,*args,**kwargs):
        form = InvitationForm(self.request.POST)
        store = get_object_or_404(Store, owner=self.request.user)
        members = StoreMembers.objects.filter(store=store)
        if form.is_valid():
            invite = form.save(commit=False)
            invite.owner = self.request.user
            invite.save()
            role = form.cleaned_data.get('role')

            if role == '0':
                role_str = 'Staff'
            else:
                role_str = 'Moderator'

            current_site = get_current_site(self.request)
            mail_subject = f'Be one of my { role_str }'
            to_email = form.cleaned_data.get('invited')

            context = {
                'invite': invite,
                'domain': current_site.domain,
            }
            
            message =  render_to_string('acc_active_email.html', context)

            send_mail(
                mail_subject ,
                message,
                settings.EMAIL_HOST_USER,
                [to_email],
                fail_silently=False,
            )
            messages.success(self.request, f'Please wait for his/her reply')
        context = {
            'form' : form,
            'members' : members
        }
        return render(self.request, self.template_name, context) 


class ActivationLink(TemplateView):
    """Activation Link for Store Members."""
    template_name = 'activation-form.html'
    form = RegisterWithRoleForm

    def get(self,*args,**kwargs):
        invite = get_object_or_404(StoreInvite, token=self.kwargs.get('uidb64'))
        store = get_object_or_404(Store, owner=invite.owner)
        date = datetime.date.today() - invite.created_at.date() 

        if date.days <= 7 and not invite.is_used:
            context = super(ActivationLink, self).get_context_data(**kwargs)
            context['form'] = self.form()
            return render(self.request, self.template_name, context)
        messages.error(self.request, f'Activation link is invalid!')
        return redirect('/')

    def post(self,*args,**kwargs):
        form = RegisterWithRoleForm(self.request.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            invite = get_object_or_404(StoreInvite, token=self.kwargs.get('uidb64'))
            store = get_object_or_404(Store, owner=invite.owner)
            form.save()
            new_user = form.save(commit=False)
            new_user.email = invite.invited
            new_user.is_staff = False
            new_user.is_owner = False
            new_user.save()
            member = StoreMembers(store=store, members=new_user, role=invite.role)
            member.save()
            invite.is_used = True
            invite.save()
            messages.success(self.request, f'Your account has been created! You are now able to login.')
        return render(self.request, self.template_name, {'form': form}) 


