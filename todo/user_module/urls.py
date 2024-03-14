from django.urls import path
from user_module.views import index

urlpatterns =[
    path('',index,name='index'),
]
