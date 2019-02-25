import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from accounts.models import User

from .forms import InvitationForm, RegisterWithRoleForm
from .models import Store, StoreInvite, StoreMembers

'''
class SendInvitation(LoginRequiredMixin, TemplateView):
    """Send Invitation Link for Potential Store Members"""
    template_name = 'posts/includes/update-post-modal.html'
    form = UpdatePostForm

    def get(self,*args,**kwargs):
        if self.request.is_ajax():
            context = super(UpdateView, self).get_context_data(**kwargs)
            context['form'] = UpdatePostForm(instance=Product.objects.get(pk=self.kwargs.get('product_id')))
            context['products'] = Product.objects.filter(pk=self.kwargs.get('product_id'))
            return render(self.request, self.template_name, context)
        raise Http404

    def post(self,*args,**kwargs):
        form = UpdatePostForm(self.request.POST, instance=Product.objects.get(pk=self.kwargs.get('product_id')))
        if form.is_valid():
            form.save()
            messages.success(self.request, f'Item Updated')
            return redirect('message')
        return render(self.request, self.template_name, {'form': form}) 
'''


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
            return HttpResponse('Please wait for his/her reply')
    else:
        form = InvitationForm()
    return render(request, 'invite.html', {'form': form})


def activate_membership(request,uidb64): 
    invite = get_object_or_404(StoreInvite, token=uidb64)
    store = get_object_or_404(Store, owner=invite.owner)
    
    date = datetime.date.today() - invite.created_at.date() 
    if date.days <= 7 and not invite.is_used:
        if request.method == 'POST':
            form = RegisterWithRoleForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.email = invite.invited
                new_user.save()
                member = StoreMembers(store=store, members=new_user, role=invite.role)
                member.save()
                invite.is_used = True
                invite.save()
                #import pdb; pdb.set_trace()
            else:
                return render(request, 'activation-form.html', {'form': form})
        else:
            form = RegisterWithRoleForm()
        return render(request, 'activation-form.html', {'form': form})
    return HttpResponse('Activation link is invalid!')



