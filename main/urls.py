from django.urls import path 
from .views import TaskDetail, TaskList, TaskCreate, TaskUpdate, TaskDelete, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<str:pk>', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<str:pk>/', TaskDelete.as_view(), name='delete-task'),
]