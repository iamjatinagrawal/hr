from django.urls import path
from .views import EmployeeListView,EmployeeDeleteView,EmployeeUpdateView  #,EmployeeDetailView



app_name = 'emp'

urlpatterns = [

	path('employees/',EmployeeListView.as_view(),name='emp-list'),
	# path('employees/<pk>',EmployeeDetailView.as_view(),name='emp-detail'),
	path('employees/<pk>/delete',EmployeeDeleteView.as_view(),name='emp-delete'),
	path('employees/<pk>',EmployeeUpdateView.as_view(),name='emp-detail-update')

]