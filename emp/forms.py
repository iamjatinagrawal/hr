from .models import Employee
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class EmployeeUpdateForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['first_name','last_name',
				  'dob', 'designation',
				  'branch','email',
				  'salary','slug']


	def __init__(self, *args, **kwargs):
		super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.label_class = 'col-lg-2'
		self.helper.form_class = 'form-horizontal'
		self.helper.field_class = 'col-lg-10'
		self.helper.add_input(Submit('submit', 'Submit'))


		# self.helper.layout = Layout(
		# 						    'first_name','last_name',
		# 		  					'dob', 'designation',
		# 						    'branch','email',
		# 						    'salary','slug',
		# 						    StrictButton('Submit', css_class='btn-default'),
		# 						)	