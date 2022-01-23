from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CategoryPageView(TemplateView):
    template_name = 'category.html'

class CoursePageView(TemplateView):
    template_name = 'kurslar.html'