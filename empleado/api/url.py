from django.urls import path
from empleado.api.view import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView, DepartmentViewSet, JobViewSet

urlpatterns = [
    path('employee/',EmployeeListCreateAPIView.as_view(), name= 'Empleados'),
    path('employee/<int:pk>',EmployeeRetrieveUpdateDestroyAPIView.as_view(), name = 'empleados'),
    #path('department/', DepartmentViewset.as_view(), name = 'Departamentos'),
    #path('job/', JobViewset.as_view(), name = 'Trabajo'),
]