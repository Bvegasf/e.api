
#importo clase de autenticacion
from rest_framework import status
from django.core.checks import messages
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from users.authentication import ExpiringTokenAuthentication
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

#importo clase para obtener el token
from rest_framework.authentication import get_authorization_header



class authentication(object):
#clase de django que se ejecuta primero, y aqui se debe interrumpir la secuencia de jecucion

    user = None
    user_expired_token = False
    def get_user(self, request):
        token= get_authorization_header(request).split()

        if token:
            try:
                token=token[1].decode()
                

            except:
                return None
                
            expired_token = ExpiringTokenAuthentication()
            user,token,message,self.user_expired_token = expired_token.authenticate_credentials(token)
            if user != None and token != None:
                self.user = user
                return user

            return message

        return None



    def dispatch(self, request, *args, **kwargs):

        user = self.get_user(request)

        # se encontro token en la peticion
        if user is not None:
            if type(user) == str:
                # si el response es cadena de caracter ocurrio un error
                 response = Response({'error':user, 'expired':self.user_expired_token},
                                                    status=status.HTTP_401_UNAUTHORIZED)
                 response.accepted_renderer = JSONRenderer()
                 response.accepted_media_type = 'application/json'
                 response.renderer_context = {}
                 return response

            if not self.user_expired_token:
                return super().dispatch(request, *args, **kwargs)


        response = Response({'error':'no se han enviado las credenciales requeridas.' ,
                                                    'expired':self.user_expired_token},
                                                    status=status.HTTP_400_BAD_REQUEST)

        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}

        return response



    