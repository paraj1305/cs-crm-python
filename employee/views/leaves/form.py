# from django import forms
# from employee.models import Leave

# class LeaveForm(forms.ModelForm):
#     class Meta:
#         model = Leave
#         fields = ['leave_date', 'leave_reason']
#         widgets = {
#            'leave_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'leave_reason': forms.TextInput(attrs={'class': 'form-control'}),
#         }
       
from django import forms
from employee.models import Leave

class LeaveForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'start-date', 'type': 'text'}),
        label='Start Date',
        required=True
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'end-date', 'type': 'text'}),
        label='End Date',
        required=True
    )
    
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'leave_reason']
        widgets = {
            'leave_reason': forms.TextInput(attrs={'class': 'form-control'}),
        }
