from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('module/<slug:slug>/', GetModule.as_view(), name='module'),

]