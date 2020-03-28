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
