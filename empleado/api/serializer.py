from django.db.models import fields
from empleado.models import *
from rest_framework import serializers

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        exclude=('state','created_date','modified_date','delete_date')


    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'last_name':instance.last_name,
            
            'job': instance.job.description if instance.job.description is not None else '',
            'department':Departmentserializer(instance.job.department).data if Departmentserializer(instance.job.department).data is not None else '',
            
        }
        

class Departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        exclude=('state','created_date','modified_date','delete_date','id')

    


class Jobserializer(serializers.ModelSerializer):
    class Meta:
        model= Job
        exclude=('state','created_date','modified_date','delete_date')

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'description':instance.description,
            'department':instance.department.name if instance.department.name is not None else ''
        }


        

