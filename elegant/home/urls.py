
from django.urls import path
from .views import homePage,contactSubmit

urlpatterns = [

    path('',homePage),
    path('contact-submit',contactSubmit)

]