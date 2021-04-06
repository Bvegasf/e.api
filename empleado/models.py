
from django.db import models
from django.db.models.deletion import CASCADE
from base.models import BaseModel, models

# Create your models here.
class Department(BaseModel):
    name=models.CharField('nombre',max_length=20)
    description=models.CharField('descripcion',max_length=200,blank=True)
    code=models.IntegerField('codigo',max_length=7)



    class Meta:

        verbose_name= 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.name

class Job(BaseModel):
    description = models.CharField('descripcion', max_length=100)
    department = models.ForeignKey(Department, on_delete=CASCADE, verbose_name= 'Puesto de Trabajo', null= True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.description

class Employee(BaseModel):
    
    name = models.CharField('name', max_length=50)
    last_name = models.CharField('apellido',max_length=50)
    ci = models.IntegerField('cedula',unique=True)
    email = models.EmailField('email',unique=True)
    is_active = models.BooleanField('Esta activo', default= True)
    # Department = models.ForeignKey(Department, on_delete=CASCADE,verbose_name='departamento', null= True)
    job = models.ForeignKey(Job, on_delete=CASCADE, verbose_name = 'role', null = True)
    image = models.ImageField(upload_to='employee/', blank=True, null= True)

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'Nombre: {self.name}  Apellido: {self.last_name}'





