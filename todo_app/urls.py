from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    path('updateTask/<task_id>', views.updateTask, name='updateTask'),
    path('deleteTask/<task_id>', views.deleteTask, name='deleteTask'),
    path('viewTask/<task_id>', views.viewTask, name='viewTask'),
    path('login/', auth_views.LoginView.as_view(template_name='todo_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),  # URL for registration
    path('add/', views.addTask, name='addTask'),
]