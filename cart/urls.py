from django.urls import path
from .views import *

urlpatterns = [
 
    path('',CartView.as_view(),name='cart'), 
    path('send_email/',SendEmail.as_view(),name='send_email'),
    path('createfactor/<int:id>',CreateFactor.as_view(),name='createfactor'),
    
]
