# employee/urls.py
from django.urls import path
from .views.authentication.loginviews import employee_login, home_view, employee_logout, employee_password_reset,project_list,projects
from .views.taskviews import employee_tasks,task_detail
from .views.leaveviews import apply_leave,leaves
app_name = 'employee'
urlpatterns = [

    #login urls
    path('login/', employee_login, name='employee_login'),
    path('home/', home_view, name='home_view'),
    path('reset-password/', employee_password_reset, name='employee_password_reset'),
    path('logout/', employee_logout, name='employee_logout'),

    #projects urls
    path('project/', project_list, name='project_list'),
    path('projects/<int:project_id>/',projects, name='projects'),

    #tasks urls
    path('tasks/', employee_tasks, name='employee_tasks'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),  # Add this URL pattern for task details
    
    # leaves url
    path('apply-leave/', apply_leave, name='apply_leave'),
    path('leavs/', leaves, name='leaves'),
    

   

]
