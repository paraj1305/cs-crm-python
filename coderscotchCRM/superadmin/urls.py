# superadmin/urls.py
from django.urls import path
from .views.admin import views, clientViews, employeeview, projectviews,taskviews,leadsviews,leavesview,invoiceviews
from django.conf import settings
from django.conf.urls.static import static



app_name = 'superadmin'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('create-superadmin/', views.edit_superadmin, name='edit_superadmin'),
    path('profile/', views.admin_profile, name='admin_profile'),
    # Client URLs
    path('clients/', clientViews.client_list, name='client_list'),
    path('clients/create/', clientViews.client_create, name='client_create'),
    path('clients/update/<int:pk>/', clientViews.client_update, name='client_update'),
    path('clients/delete/<int:client_id>/', clientViews.client_delete, name='client_delete'),
    path('clients/bulk-delete/', clientViews.bulk_client_delete, name='bulk_client_delete'),
    path('clients/upload_images/', clientViews.upload_client_images, name='upload_client_images'),
    path('clients/details/<int:client_id>/', clientViews.client_detail, name='client_detail'),

    # Employee URLs
    path('employees/', employeeview.employee_list, name='employee_list'),
    path('employees/create/', employeeview.employee_create, name='employee_create'),
    path('employees/update/<int:pk>/', employeeview.employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', employeeview.employee_delete, name='employee_delete'),
    path('employees/upload-images/', employeeview.upload_employee_images, name='upload_employee_images'),
    path('employees/delete/<int:pk>/', employeeview.employee_delete, name='employee_delete'),
    path('employees/bulk-delete/', employeeview.bulk_employee_delete, name='bulk_employee_delete'),
    path('employees/details/<int:employee_id>/', employeeview.employee_detail, name='employee_detail'),
    path('salary-slip/<int:salary_slip_id>/pdf/', employeeview.generate_salary_slip_pdf, name='salary_slip_pdf'),
    path('salary_slip/<int:salary_slip_id>/delete/', employeeview.delete_salary_slip, name='delete_salary_slip'),

    
    path('employee/<int:employee_id>/create-slip/', employeeview.check_or_create_salary_slip, name='check_or_create_salary_slip'),
    path('employee/<int:employee_id>/create-salary-slip/', employeeview.create_salary_slip, name='create_salary_slip'),
    path('salary_slip/<int:salary_slip_id>/', employeeview.salary_slip_detail, name='salary_slip_detail'),
    path('salary_slip/<int:salary_slip_id>/update-slip/', employeeview.update_salary_slip, name='update_salary_slip'),


    # Project URLs
    path('projects/', projectviews.project_list, name='project_list'),
    path('projects/create/', projectviews.project_create, name='project_create'),
    path('projects/<int:project_id>/edit/', projectviews.project_update, name='project_update'),
    path('projects/delete/<int:project_id>/', projectviews.project_delete, name='project_delete'),
    path('projects/bulk-delete/', projectviews.bulk_project_delete, name='bulk_project_delete'),
    path('projects/<int:project_id>/', projectviews.project_detail, name='project_detail'),
    path('projects/<int:project_id>/change-request/', projectviews.change_request_create, name='change_request_create'),
    path('projects/upload_files/', projectviews.upload_project_filess, name='upload_project_filess'),

    #Task URLS
    # path('tasks/', taskviews.task_list, name='task_list'),
   
    path('kanban/', taskviews.kanban_board, name='kanban_board'),
    path('task/create/', taskviews.create_task, name='create_task'),
    path('task/update/<int:task_id>/', taskviews.update_task, name='update_task'),
    path('tasks/<int:task_id>/delete/', taskviews.task_delete, name='task_delete'),
    path('tasks/<int:task_id>/detail/', taskviews.task_detail, name='task_detail'),
    path('tasks/add_board/', taskviews.add_board, name='add_board'),
    path('kanban/edit_board/<int:board_id>/', taskviews.edit_board, name='edit_board'),
    path('kanban/delete_board/<int:board_id>/', taskviews.delete_board, name='delete_board'),
    path('update_task_board/<int:task_id>/', taskviews.update_task_board, name='update_task_board'),
    path('upload-task-files/', taskviews.upload_task_filess, name='upload_task_filess'),
    
    #Leads urls
    path('leads/', leadsviews.lead_list, name='lead_list'),
    path('leads/<int:pk>/', leadsviews.lead_detail, name='lead_detail'),
    path('leads/create/', leadsviews.lead_create, name='lead_create'),
    path('leads/update/<int:pk>/', leadsviews.lead_update, name='lead_update'),
    path('leads/delete/<int:lead_id>/', leadsviews.lead_delete, name='lead_delete'),
    path('leads/bulk-delete/', leadsviews.bulk_lead_delete, name='bulk_lead_delete'),
    path('leads/upload_files/', leadsviews.upload_lead_filess, name='upload_lead_filess'),
    
    # leaves urls
    path('leave-management/', leavesview.leave_management, name='leave_list'),  # For listing all leaves
    path('leave-management/<int:leave_id>/', leavesview.leave_management, name='leave_approval'), 
    
    # invoice urls
    path('invoices/', invoiceviews.invoice_list, name='invoice_list'),
    path('invoice/<int:invoice_id>/', invoiceviews.invoice_detail, name='invoice_detail'),
    path('invoices/create/', invoiceviews.invoice_create, name='invoice_create'),
    path('invoices/add_item/', invoiceviews.add_invoice_item, name='add_invoice_item'),
    path('invoice/<int:invoice_id>/edit/', invoiceviews.invoice_edit, name='invoice_edit'),
    path('invoice/<int:invoice_id>/delete/', invoiceviews.invoice_delete, name='invoice_delete'),
    path('invoice/<int:invoice_id>/item/create/', invoiceviews.invoice_item_create, name='invoice_item_create'),
    path('invoice/<int:invoice_id>/item/<int:item_id>/delete/', invoiceviews.invoice_item_delete, name='invoice_item_delete'),
    path('invoice/<int:invoice_id>/send/', invoiceviews.send_invoice_pdf, name='send_invoice_pdf'),
    path('invoice/<int:invoice_id>/download/', invoiceviews.download_invoice_pdf, name='download_invoice_pdf'),
    
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
