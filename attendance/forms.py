from django import forms
from django.forms import widgets


class AttendanceForm(forms.Form):
    name = forms.CharField(max_length=20, label='Employee Name',widget=widgets.TextInput(attrs={'placeholder':'Enter Name','class':'form-control'}))
    date = forms.DateField(label='Entry Date',widget=widgets.DateInput(attrs={'type':'date','class':'form-control'}))
    is_present = forms.BooleanField(label='Is Present', required=False)
    check_in_time = forms.DateTimeField(label='Check In',widget=widgets.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))
    check_out_time = forms.DateTimeField(label='Check Out',widget=widgets.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}))