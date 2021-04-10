from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework import status
from location.api.serializer import ContinentalRegionModelSerializer, CountryModelSerializer, CityModelSerializer
from rest_framework import viewsets


class ContinentalRegionListCreatedAPIView(generics.ListCreateAPIView):

    serializer_class = ContinentalRegionModelSerializer
    queryset = ContinentalRegionModelSerializer.Meta.model.objects.all()
    

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializers.is_valid():
            serializer.save()
            return Response({'message':'El continente fue registrado con exito'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ContinentalRegionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContinentalRegionModelSerializer

    def get_queryset(self, pk= None):

        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id = pk).firts()

    def delete(self,request, pk= None):

        continental = self.get_queryset().Meta.objects.filter(id = pk).firts()
        if continental:
            continental.delete()
            return Response({'message':'El continente fue eliminado con exito'},status=status.HTTP_200_OK)

        return Response({'error':'los datos ingresado no son correcto'}, status = status.HTTP_400_BAD_REQUEST) 

    
class CountryModelViewset(viewsets.ModelViewSet):
    serializer_class = CountryModelSerializer

    def get_queryset(self, pk = None ):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()

        return self.get_serializer().Meta.model.objects.filter(id=pk).firts()



    def list(self, request):
        products_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(products_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializers= self.serializer_class(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'mesagge':'El pais fue registrado con exito'},status=status.HTTP_201_CREATED)

        


        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CityModelViewset(viewsets.ModelViewSet):
    serializer_class = CityModelSerializer

    def get_queryset(self, pk = None ):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()

        return self.get_serializer().Meta.model.objects.filter(id=pk).firts()

    





