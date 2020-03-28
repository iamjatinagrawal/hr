from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (EmployeeListView,
					EmployeeDeleteView,
					EmployeeUpdateView,
					EmployeeCreateView) #,EmployeeDetailView



app_name = 'emp'

urlpatterns = [

	path('employees/',login_required(EmployeeListView.as_view()),name='emp-list'),
	path('employees/create',EmployeeCreateView.as_view(),name='emp-create'),
	# path('employees/<pk>',EmployeeDetailView.as_view(),name='emp-detail'),
	path('employees/<pk>/delete',EmployeeDeleteView.as_view(),name='emp-delete'),
	path('employees/<pk>',EmployeeUpdateView.as_view(),name='emp-detail-update'),

]