from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Employee
from django.urls import reverse_lazy,reverse
from .forms import EmployeeUpdateForm


class EmployeeListView(ListView):
	model = Employee
	template_name = 'emp/index.html'
	queryset = Employee.objects.all()
	context_object_name = 'emp_list'


# class EmployeeDetailView(DetailView):
# 	model = Employee
# 	template_name = 'emp/emp_detail.html'

# 	def get_object(self,*args,**kwargs):
# 		emp_id = self.kwargs.get('pk')

# 		try:
# 			obj = Employee.objects.get(id=emp_id)
# 			return obj
# 		except Http404:
# 			raise Http404("Employee with the given id doesn't exists")


class EmployeeDeleteView(DeleteView):
	model = Employee
	success_url = reverse_lazy('emp:emp-list')
	template_name = 'emp/emp_confirm_delete.html'


class EmployeeUpdateView(UpdateView):
	model = Employee
	template_name = 'emp/emp_update_form.html'
	# fields = ['first_name',
	# 		  'last_name',
	# 		  'designation',
	# 		  'salary']

	form_class = EmployeeUpdateForm
	

	def get_success_url(self,**kwargs):
		print(self.object.id)
		return reverse_lazy('emp:emp-detail-update',kwargs={'pk':self.object.id})






