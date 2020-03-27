from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator


class Employee(models.Model):

	alpha = RegexValidator(r'^[a-zA-Z ]*$', 'Please enter valid data')

	first_name = models.CharField(max_length=50, validators=[alpha])
	last_name = models.CharField(max_length=50, validators=[alpha])
	dob = models.DateField(help_text='YYYY-MM-DD')
	designation = models.CharField(max_length=50, validators=[alpha])
	branch = models.CharField(max_length=50, validators=[alpha])
	email = models.EmailField()
	salary = models.IntegerField()
	slug = models.SlugField(unique=True, default="slug")

	def __str__(self):
		return self.first_name+" "+self.last_name

	@property
	def full_name(self):
		return self.first_name+" "+self.last_name

	def save(self,*args,**kwargs):
		self.slug = slugify(self.first_name)
		super(Employee, self).save(*args,**kwargs)


#e = Employee.objects.create(first_name='Nihar',last_name='Agarwal',designation='React Developer', branch='Delhi', dob='1998-12-17', salary=2, email='nihar@nihar.com')
#e = Employee.objects.create(first_name='Puru',last_name='Chandra',designation='Flutter Developer', branch='Pune', dob='1995-03-28', salary=3, email='puru@tradexa.co.in')
#e = Employee.objects.create(first_name='Parmesh',last_name='Bhande',designation='Python Developer', branch='Pune', dob='1994-01-02', salary=4, email='parmesh@tradexa.co.in')
#e = Employee.objects.create(first_name='Ramesh',last_name='Jhajharia',designation='CEO', branch='Pune', dob='1900-03-03', salary=0, email='ramesh@tradexa.co.in')
#e = Employee.objects.create(first_name='Amrit',last_name='Khandelwal',designation='Sales Manager', branch='Pune', dob='1986-01-15', salary=100, email='amrit@imaginext.co.in')