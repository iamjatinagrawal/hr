from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Employee
from django.urls import reverse_lazy,reverse
from .forms import EmployeeForm, EmployeeUpdateForm


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


class FormActionMixin(object):

    def post(self, request, *args, **kwargs):
        """Add 'Cancel' button redirect."""
        if "delete" in request.POST:
        	url = reverse('emp:emp-delete',kwargs={'pk':kwargs['pk']})# or e.g. reverse(self.get_success_url())
        	return HttpResponseRedirect(url)
        elif "create" in request.POST:
        	url = reverse('emp:emp-create')# or e.g. reverse(self.get_success_url())
        	return HttpResponseRedirect(url)
        elif "cancel" in request.POST:
        	url = reverse('emp:emp-list')# or e.g. reverse(self.get_success_url())
        	return HttpResponseRedirect(url)
        else:
        	return super(FormActionMixin, self).post(request, *args, **kwargs)


class EmployeeUpdateView(FormActionMixin,UpdateView):
	model = Employee
	template_name = 'emp/emp_update_form.html'
	# fields = ['first_name',
	# 		  'last_name',
	# 		  'designation',
	# 		  'salary']

	form_class = EmployeeUpdateForm

	def get_success_url(self,**kwargs):
		return reverse_lazy('emp:emp-detail-update',kwargs={'pk':self.object.id})





class EmployeeCreateView(FormActionMixin,CreateView):
	model = Employee
	template_name = 'emp/emp_create.html'
	form_class = EmployeeForm

	def get_success_url(self,**kwargs):
		return reverse_lazy('emp:emp-detail-update',kwargs={'pk':self.object.id})
		






