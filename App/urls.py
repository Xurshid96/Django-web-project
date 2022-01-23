from django.urls import path
from .views import HomePageView, AboutPageView, CategoryPageView, CoursePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('category/', CategoryPageView.as_view(), name='category'),
    path('course/', CoursePageView.as_view(), name='course'),
]