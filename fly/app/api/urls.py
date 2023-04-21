from django.urls import path
from .views import *

app_name = 'modules'

urlpatterns = [
    path('modules/', ModuleList.as_view(), name='module_list'),
    path('modules/<int:pk>/', ModuleDetail.as_view(), name='module_detail'),
]
