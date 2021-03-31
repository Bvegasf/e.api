from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework import viewsets
from empleado.api.serializer import Employeeserializer, Departmentserializer, Jobserializer



class EmployeeListCreateAPIView(generics.ListCreateAPIView):

    serializer_class= Employeeserializer
    queryset=Employeeserializer.Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'El empleado se registro con exito'}, status= status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = Employeeserializer

    
    def get_queryset(self, pk=None):

        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk ,state=True).first()
        
    def delete(self, request ,pk=None):
        empleado = self.get_queryset().filter(id=pk).first()
        if empleado:
            empleado.state=False
            empleado.save()
            return Response({'message':'El empleado fue eliminado con exito del sistema'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'No existe un empleado registraodo que coincida con los datos ingresados'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):

        if self.get_queryset(pk):
            employee_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(employee_serializer.data, status = status.HTTP_200_OK)

        return Response({'message':'No existe un empleado con los datos ingresado'}, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk = None):
        if self.get_queryset(pk):

            employee_serializer = self.serializer_class(self.get_queryset(pk, data=request.data))
            if employee_serializer.is_valid():
                employee_serializer.save()
                return Response(employee_serializer.data, status = status.HTTP_200_OK)

            return Response(employee_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DepartmentViewset(viewsets.ModelViewSet):
    serializer_class = Departmentserializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def list(self, request):
        department_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(department_serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
         serializer= self.serializer_class(data= request.data)
         if  serializer.is_valid():
            serializer.save()
            return Response({'mesage':'Departamento creado correctamente'},status=status.HTTP_201_CREATED)
         
         
         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def update(self,request,pk= None):
         if self.get_queryset(pk):
            department_serializer= self.serializer_class(self.get_queryset(pk), data= request.data)
            if department_serializer.is_valid():
                department_serializer.save()
                return Response(department_serializer.data,status=status.HTTP_200_OK)
            return Response(department_serializer.errors, status= status)


    def destroy(self,request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state=False
            product.save()
            return Response({'mesage':'El departamento fue eliminado con exito'},status.HTTP_200_OK)
        return Response({'errors':'No existe un departamento con los datos especificados'},status.HTTP_400_BAD_REQUEST)

    


    


class JobViewset(viewsets.ModelViewSet):
    serializer_class = Jobserializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()


