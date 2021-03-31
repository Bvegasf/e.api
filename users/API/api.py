
from decimal import Context
from django.http import response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from users.API.serializer import UserSerializer, UserListserializer

# decorador
@api_view(['GET','POST'])

# como es una funcion se le pasa el parametro request

def user_api_view(request):

    # si es un metodo http GET realiza la peticion y muestra la informacion

    if request.method == 'GET':
        user = User.objects.all().values('id', 'username','email','password')
        User_serializer = UserListserializer(user,many = True)

        #test_data ={
            #'name':'thiago',
            #'email':'Thiago@example.com',
            #'last_name':'Vegas',
            #'username':'Tvegas',
            #'is_super_user':'true'


        #}
        # al serializdor se le puede pasar context para que contenga todo el Json
        #test_user= TestUserserializer(data= test_data, context=test_data)

        #Al hacer validacion se crea un metodo que verifique que los datos enviados cumplan con 
        #los campos del serializador

        #if test_user.is_valid():
            #  se llama a la funcion create si es valido


            #test_instance= test_user.save()
            #print("Paso validaciones")




        return Response(User_serializer.data, status= status.HTTP_200_OK)

# si es un metodo post realiza el guardado de la informacion, primero verifica si lo que se le paso es valido
# si es valido se procede a guardar, si no, muestra un error enviado como diccionario

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'mesage':'El usuario fue creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])

#esta funcion sirve para mostrar detalles de la informacion de un usuario
#esta muestra una sola instancia y se usa para actualizar, mostrar o eliminar informacion

def user_detail_view(request,pk=None):
    #consulta setquery
    user = User.objects.filter(id=pk).first()
    #validacion de consulta, si existe procede a realizar el otro codigo
    if user:

        if request.method == 'GET':
      
            user_serializer= UserSerializer(user)
            return Response(user_serializer.data, status= status.HTTP_200_OK)

        #Luego se coloca el codigo para hacer la actualizacion.
        #update

        elif request.method == 'PUT':
           
            user_serializer=UserSerializer(user, data= request.data)
            #verifica si el serializador cumple con los requisitos, si es asi guarda la informacion

            if user_serializer.is_valid():

               user_serializer.save()
               return Response(user_serializer.data, status= status.HTTP_200_OK)

            return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        #para eliminar se hace otro elif
        elif request.method =='DELETE':
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({'mesage':'Usuario eliminado correctamente'}, status= status.HTTP_200_OK)

    return Response({'mesage':'El usuario ingresado no se encuentra registrado'}, status= status.HTTP_404_NOT_FOUND)
