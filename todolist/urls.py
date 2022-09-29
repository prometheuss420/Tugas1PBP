from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-task/', add_task, name='add_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('change-status/<int:id>', change_status, name='change_status'),
   
]