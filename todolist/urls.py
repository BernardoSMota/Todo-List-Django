from django.urls import path
from todolist.views import index, completed, pending, changeCompleteStatus, delete, createTask, editTask

app_name = 'todo'

urlpatterns = [
    path('', index , name='index'),
    path('completed/', completed , name='completed'),
    path('pending/', pending , name='pending'),
    path('change/<int:id>/', changeCompleteStatus , name='changeCompleteStatus'),
    path('delete/<int:id>/', delete , name='delete'),
    path('create-task/', createTask , name='create'),
    path('edit-task/<int:id>/', editTask , name='edit'),
]