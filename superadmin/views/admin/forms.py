
from django import forms
from superadmin.models import Superadmin,Client,Employee,Project,ChangeRequest,Task,Board,Lead,Invoice,InvoiceItem,ClientImage,ProjectFile,EmployeeImage,LeadFile,SalarySlip
import re,datetime

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

class SuperadminForm(forms.ModelForm):
    class Meta:
        model = Superadmin
        fields = ['email', 'company_name', 'address','bank', 'bank_no', 'SWIFT_CODE', 'IFSC_CODE', 'logo', 'website']
     
        labels = {
            'SWIFT_CODE': 'SWIFT Code',
            'IFSC_CODE': 'IFSC Code',
        }
        
        password = forms.CharField(required=False, widget=forms.PasswordInput)

    def save(self, commit=True):
        superadmin = super(SuperadminForm, self).save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            superadmin.set_password(password)  # Hash the password before saving
        if commit:
            superadmin.save()
        return superadmin
        
# Client management
from django.forms import modelformset_factory

class ClientForm(forms.ModelForm):
    class Meta:
        current_year = datetime.datetime.now().year
        model = Client
        fields = ['name', 'email', 'phone', 'location', 'industry', 'website', 'since', 'company', 'address']
        widgets = {
            'since': forms.Select(choices=[(year, year) for year in range(2015, current_year + 1)]),
            'address': forms.Textarea(attrs={'rows': 2}),
        }

class ClientImageForm(forms.ModelForm):
    class Meta:
        model = ClientImage
        fields = ['image']

# Formset for multiple image uploads
ClientImageFormSet = modelformset_factory(ClientImage, form=ClientImageForm, extra=3)

# Employee management
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email', 'phone','joining_date', 'salary', 'designation'
        ]
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            
        }
class EmployeeImageForm(forms.ModelForm):
    class Meta:
        model = EmployeeImage
        fields = ['image']

# Formset for multiple image uploads
ClientImageFormSet = modelformset_factory(ClientImage, form=ClientImageForm, extra=3)


# Project management model
class ProjectForm(forms.ModelForm):
    project_files = forms.FileField(widget=forms.FileInput(), required=False)
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'})
    )
    
    class Meta:
        model = Project
        fields = [
            'project_title', 'client', 'priority', 'status',
             'start_date', 'deadline', 'project_cost', 'employees'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'employees': forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}),
            
        }

class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['file']

# Formset for multiple image uploads
ProjectFileFormSet = modelformset_factory(ProjectFile, form=ProjectFileForm, extra=3)
        

class ChangeRequestForm(forms.ModelForm):
    class Meta:
        model = ChangeRequest
        fields = ['project', 'task', 'hours','cost']
       
    def clean_hours(self):
        hours = self.cleaned_data.get('hours')
        pattern = re.compile(r'^\d+\s*(hours?|days?|minutes?|weeks?|seconds?)$')
        if not pattern.match(hours):
            raise forms.ValidationError('Invalid duration format. Please use "2 hours", "3 days", "10 minutes", etc.')
        return hours
    
#Task form
class TaskForm(forms.ModelForm):
    board = forms.ModelChoiceField(queryset=Board.objects.all(), required=True, empty_label="Select a Board")
    class Meta:
        model = Task
        fields = ['title', 'project','board', 'description', 'due_date', 'employee', 'priority', 'status']

        
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 1}), 
           
        }

#lead form
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['project_name', 'company', 'email', 'phone', 'project_type', 'location', 'description', 'Timeline', 'budget']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}), 
            'Timeline': forms.DateInput(attrs={'type': 'date'}),
        }

class LeadFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ['file']

# Formset for multiple image uploads
ProjectFileFormSet = modelformset_factory(LeadFile, form=LeadFileForm, extra=3)
        

        
#invoice form
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'invoice_date', 'payment_status','tax_percentage']
        widgets = {
           'invoice_date' : forms.DateInput(attrs={'type': 'date'}),
        }

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['title', 'rate']
        
        
class SalarySlipForm(forms.ModelForm):
    class Meta:
        model = SalarySlip
        fields = ['month', 'year', 'professional_tax', 'TDS', 'leave_deduction']
        widgets = {
            'month': forms.Select(choices=SalarySlip.MONTH_CHOICES),
            'year': forms.Select(choices=SalarySlip.YEAR_CHOICES),
        }
        
class ReportFilterForm(forms.Form):
    current_year = datetime.datetime.now().year
    YEAR_CHOICES = [('yearly', 'All Year')] + [(year, year) for year in range(2015, current_year + 1)] 
    MONTH_CHOICES = [('', 'All Months')] + [
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
    ]
    chart_type = forms.ChoiceField(
        choices=[
            ('bar', 'Bar'),
            ('line', 'Line'),
            ('pie', 'Pie'),
            ('doughnut', 'Doughnut'),
            ('polarArea', 'Polar Area'),
            ('radar', 'Radar'),
            ('bar', 'Bar'),
           
        ],
        required=False,
        initial='bar'  # Set default chart type to 'bar'
    )
    
    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        required=False,
        label='Year',
        initial='yearlt'  # Set default year to 'yearly'
    )
    month = forms.ChoiceField(choices=MONTH_CHOICES, required=False, label='Month')