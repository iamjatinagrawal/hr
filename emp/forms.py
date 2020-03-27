from .models import Employee
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
# from django.core.validators import RegexValidator


class EmployeeUpdateForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ['first_name','last_name',
				  'dob', 'designation',
				  'branch','email',
				  'salary']

    
	def __init__(self, *args, **kwargs):
		super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.label_class = 'col-lg-2'
		self.helper.form_class = 'form-horizontal'
		self.helper.field_class = 'col-lg-10'
		self.helper.add_input(Submit('submit','Save',))
		self.helper.add_input(Submit('delete', 'Delete', css_class='btn-danger'))
		self.helper.add_input(Submit('create', 'Create a new record', css_class='btn-outline-secondary'))



class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['first_name','last_name',
				  'dob', 'designation',
				  'branch','email',
				  'salary']

    
	def __init__(self, *args, **kwargs):
		super(EmployeeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.label_class = 'col-lg-2'
		self.helper.form_class = 'form-horizontal'
		self.helper.field_class = 'col-lg-10'
		self.helper.add_input(Submit('submit','Save'))
