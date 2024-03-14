from django.urls import path
from user_module.views import index,update_task,delete_task
#from .views import login



urlpatterns =[
   path('', index, name='index'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task')
]
