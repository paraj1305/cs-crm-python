from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from employee.models import Leave
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.apps import apps


class SuperadminManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)  # Use Django's set_password method
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class Superadmin(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100, null=True)
    bank = models.CharField(max_length=100, null=True)
    bank_no = models.IntegerField(null=True)
    SWIFT_CODE = models.CharField(max_length=100, null=True)
    IFSC_CODE = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='logo/', null=True)
    website = models.CharField(max_length=100, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = SuperadminManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



# client models
INDUSTRY_CHOICES = [
    ('Tech', 'Tech'),
    ('Finance', 'Finance'),
    ('Healthcare', 'Healthcare'),
    ('Education', 'Education'),
    ('Other', 'Other'),
]

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    location = CountryField()
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    website = models.URLField()
    since = models.PositiveIntegerField()
    company = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name

class ClientImage(models.Model):
    client = models.ForeignKey(Client, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='client_images/')
    
    def __str__(self):
        return f"Image for {self.client.name}"

# employee model
class EmployeeManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, first_name, last_name, password, **extra_fields)

class Employee(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    # img = models.ImageField(upload_to='employee_images/', blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    total_leaves = models.IntegerField(default=20)
    designation = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    has_reset_password = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
       return f"{self.first_name} {self.last_name}"
    
    def get_leaves(self):
        Leave = apps.get_model('employee', 'Leave')
        return Leave.objects.filter(employee=self)
    # def __str__(self):
    #     return self.user.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    groups = models.ManyToManyField(Group, related_name='employee_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='employee_permissions')
    
# Model to store images related to an Employee
class EmployeeImage(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='employee_images/')



# project model
from django.conf import settings
class Project(models.Model):
    PROJECT_TYPES = [
        ('internal', 'Internal'),
        ('external', 'External'),
    ]
    PRIORITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_LEVELS = [
        ('inprogress', 'inprogress'),
        ('Complated', 'Complated'),    
    ]
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    priority = models.CharField(max_length=50, choices=PRIORITY_LEVELS, default="medium")
    status = models.CharField(max_length=50, choices=STATUS_LEVELS, default="inprogress")
    start_date = models.DateField()
    deadline = models.DateField()
    project_cost = models.DecimalField(max_digits=10, decimal_places=2)
    employees = models.ManyToManyField(Employee, related_name='projects')
    project_files = models.FileField(upload_to='project_files/', blank=True, null=True)



    def __str__(self):
        return self.project_title

    def is_assigned_to_employee(self, employee):
        """
        Check if the given employee is assigned to this project.
        """
        return self.employees.filter(id=employee.id).exists()
    
class ProjectFile(models.Model):
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files/')

    def __str__(self):
        return f"Image for {self.project.project_title}"
    
class ChangeRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.TextField()
    hours = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.project.project_name} - Change Request"

#Task management models


class Board(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
       ('unassigned', 'Unassigned'),
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('inreview', 'In Review'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField()
    attachment = models.FileField(upload_to='task_attachments/', blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default="medium")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="inprogress")

    def __str__(self):
        return self.title
    
class TaskFile(models.Model):
    task = models.ForeignKey(Task, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='task_files/',blank=True, null=True)
   
    def __str__(self):
        return f"Image for {self.lead.task_name}"
    
#Leads management model
class Lead(models.Model): 
    project_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    project_type = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    location = CountryField()
    description = models.TextField(blank=True, null=True)
    Timeline = models.DateField()
    # lead_files = models.FileField(upload_to='lead_files/', blank=True, null=True)
    budget = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.project_name}"
    
class LeadFile(models.Model):
    lead = models.ForeignKey(Lead, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='lead_files/')
   
    def __str__(self):
        return f"Image for {self.lead.project_name}"

class LeaveAdmin(models.Model):
    leave = models.OneToOneField(Leave, on_delete=models.CASCADE, primary_key=True)
    admin_notes = models.TextField(blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Leave ID: {self.leave.id} - Admin Approval"
    
    
class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_date = models.DateField(default=now)
    sent_to_client = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, choices=[
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ], default='unpaid')
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Invoice #{self.id} for {self.client.name}"

    def total_amount(self):
        return sum(item.rate for item in self.items.all())
    def total_with_tax(self):
        total = self.total_amount()
        tax_amount = (self.tax_percentage / 100) * total
        return total + tax_amount

# models.py

# models.py

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2,default=1)

    def __str__(self):
        return self.title

