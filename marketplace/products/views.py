import datetime

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import Http404
from django.views.generic import TemplateView , DetailView, ListView,View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PostForm, ImageFieldForm
from .models import Product , Category, ProductAlbum


# Create your views here.
class PostView(LoginRequiredMixin, TemplateView):
    """Create a Product"""
    template_name = 'includes/create-post-modal.html'
    form = PostForm
    i_form = ImageFieldForm
    #s_form = StockForm

    def get_context_data(self, **kwargs):
        #if self.request.is_ajax():
        context = super(PostView, self).get_context_data(**kwargs)
        context['form'] = self.form()
        context['i_form'] = self.i_form()
        #context['s_form'] = self.s_form()
        return context
        #raise Http404

    def post(self,*args,**kwargs):
        form = self.form(self.request.POST)
        #s_form = self.s_form(self.request.POST)
        i_form = ImageFieldForm(self.request.POST, self.request.FILES)

        if form.is_valid() and i_form.is_valid():
            product = form.save(commit=False)
            #product.seller = self.request.user
            product.save()
    
            #stock = s_form.save(commit=False)
            #stock.stock_no = "Stock#" +  str(datetime.datetime.now())
            #stock.product = product
            #stock.stock_on_hand = s_form.cleaned_data.get('stock_total')
            #stock.save()

            messages.success(self.request, f'Successfully Added a New Item')
            return redirect('message')        
        return render(self.request, self.template_name,{'form': form , 'i_form': i_form })