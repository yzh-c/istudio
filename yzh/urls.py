
from django.urls import path
from yzh.views import *

urlpatterns = [
    #path('main/', bcd, name='print'),
    path('register/', abc, name='regi'),
    path('login/', my_print, name='logi'),
]

