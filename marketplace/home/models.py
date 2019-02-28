from django.db import models
from products.models import Product

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.models import Collection, Page

class HomePage(Page):

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        products = Product.objects.filter(status='1', is_draft=False)
        context['products'] = products
        #import pdb; pdb.set_trace()
        return context