from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home" ),
    path('us',us,name='us'),
    path('tech',tech,name='tech'),
    path('entertainment',entertainment,name='entertainment'),
    path('science',science,name='science'),
    path('sports',sports,name='sports'),
    
]
