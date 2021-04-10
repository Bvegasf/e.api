
from rest_framework import serializers,generics
from rest_framework.response import Response
from rest_framework import status
from base.api import GeneraListApiView
from products.api.serializer.products_serializer import Productsserializer
from rest_framework import viewsets
from users.authentication_mixing import authentication



# vista de lista generica
#class ProductsListAPIView(GeneraListApiView):
    #serializer_class = Productsserializer

# vista de creacion
class ProductCreatedAPIView(generics.ListCreateAPIView):
    serializer_class=Productsserializer
    queryset= Productsserializer.Meta.model.objects.filter(state= True)

    def post(self, request):
        serializer= self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesage':'Producto creadocorrectamente'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# vista de detalle de un producto
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Productsserializer

    def get_queryset(self, pk=None):

        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk ,state=True).first()


    def delete(self, request,pk=None):

        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state=False
            product.save()
            return Response({'mesage':'El producto fue eliminado con exito'},status.HTTP_200_OK)
        return Response({'errors':'No existe un producto con los datos especificados'},status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer= self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response({'mesage':'No existe un producto con los datos ingresados'},status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None):
        if self.get_queryset(pk):
            product_serializer= self.serializer_class(self.get_queryset(pk), data= request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status= status)
            

#Clases viewset
class ProductViewset(authentication, viewsets.ModelViewSet):

    serializer_class = Productsserializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def list(self, request):
        products_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(products_serializer.data,status=status.HTTP_200_OK)


    def create(self,request):
         serializer= self.serializer_class(data= request.data)
         if  serializer.is_valid():
            serializer.save()
            return Response({'mesage':'Producto creado correctamente'},status=status.HTTP_201_CREATED)
         
         
         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def update(self,request,pk= None):
         if self.get_queryset(pk):
            product_serializer= self.serializer_class(self.get_queryset(pk), data= request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status= status)
    
    def destroy(self,request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state=False
            product.save()
            return Response({'mesage':'El producto fue eliminado con exito'},status.HTTP_200_OK)
        return Response({'errors':'No existe un producto con los datos especificados'},status.HTTP_400_BAD_REQUEST)










# <<usando vista genercas de APIView>>



# vista generica de eliminacion
#class ProductsDeleteAPIView(generics.DestroyAPIView):
   
   # serializer_class=Productsserializer
 
    #def get_queryset(self):
        #return self.get_serializer().Meta.model.objects.filter(state=True)

   # def delete(self, request,pk=None):

        #product = self.get_queryset().filter(id = pk).first()
        #if product:
            #product.state=False
            #product.save()
            #return Response({'mesage':'El producto fue eliminado con exito'},status.HTTP_200_OK)
        #return Response({'errors':'No existe un producto con los datos especificados'},status.HTTP_400_BAD_REQUEST)


#class ProductsUpdateAPIView(generics.UpdateAPIView):
   # serializer_class=Productsserializer

    #def get_queryset(self,pk):
        #return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()

    #def patch(self,request,pk=None):
        #if self.get_queryset(pk):
           # product_serializer= self.serializer_class(self.get_queryset(pk))
            #return Response(product_serializer.data, status=status.HTTP_200_OK)

        #return Response({'mesage':'No existe un producto con los datos ingresados'},status=status.HTTP_400_BAD_REQUEST)


   # def put(self, request,pk=None):
        #if self.get_queryset(pk):
           # product_serializer= self.serializer_class(self.get_queryset(pk), data= request.data)
            #if product_serializer.is_valid():
           #    # product_serializer.save()
               # return Response(product_serializer.data,status=status.HTTP_200_OK)
            #return Response(product_serializer.errors, status= status)
            
