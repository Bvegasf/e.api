from rest_framework import serializers, viewsets
from branch.api.serializer import BranchModelserializer
from branch.models import branch
from rest_framework.response import Response
from rest_framework import status
class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchModelserializer

    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()

        return self.get_serializer().Meta.model.objects.filter(id = pk).first()


    def list(self, request):
        branch_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(branch_serializer.data, status= status.HTTP_200_OK)



    def create(self, request):
        serializers = self.serializer_class(data = request.data)

        if serializers.is_valid():
            serializers.save()

            return Response({'message':'La sucursal se ha registrado con exito'}, status= status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk= None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)

            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        

        
