from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework import status
from permissions.serializer import Rolrserializer,Permissionsserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Create your views here.

class RoleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = Rolrserializer
    queryset = Rolrserializer.Meta.model.objects.all()
    permission_classes = (IsAuthenticated)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def post(self, request):
        rolserializer = self.serializer_class(data = request.data)

        if rolserializer.is_valid():
            rolserializer.save()
            return Response({'message':'se ha establecido un nuevo tipo de Rol'}, status = status.HTTP_201_CREATED)
        
        return Response(rolserializer.errors, status = status.HTTP_400_BAD_REQUEST)


class RoleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = Rolrserializer
    
    def get_queryset(self, pk= None):

        if pk is None:
            return self.get_serializer().Meta.model.objects.all()

        return self.get_serializer().Meta.model.objects.filter(id = pk). firts()

    def delete(self, request, pk= None):
         rol= self.get_queryset().filter(id=pk).firts()

         if rol:
             rol.delete()
             return Response({'message':'El rol ha sido eliminadocon exito'}, status= status.HTTP_200_OK)

         return Response({'errors':'No se encontro ningun rol con los datos especificados'}, status= status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            rol= self.serializer_class(self.get_queryset(pk))
            return Response(rol.data, status=status.HTTP_200_OK)

        return Response({'mesage':'No existe un rol con los datos ingresados'},status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None):
        if self.get_queryset(pk):
            rol= self.serializer_class(self.get_queryset(pk), data= request.data)
            if rol.is_valid():
                rol.save()
                return Response(rol.data,status=status.HTTP_200_OK)
            return Response(rol.errors, status= status)
            