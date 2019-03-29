from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class home_view(TemplateView):
    template_name = "verification/base.html"