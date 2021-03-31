
from django.core import exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from    rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone
from django.conf import Settings, settings





class ExpiringTokenAuthentication(TokenAuthentication):

    expired = False
    
    #Funcion que calcula tiempo de expiracion

    def expires_in(self,token):
        time_elapsed= timezone.now() - token.created
        left_time=timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    #funcion que indica si token expiro

    def is_token_expired(self,token):

        return self.expires_in(token) < timedelta(seconds=0)

    #funcion que llama la verificacion de tempo de expiracion

    def token_expired_handler(self,token):

        
        # si el token expiro se puede realizar una accion
        is_expire= self.is_token_expired(token)
        if is_expire:
            self.expired = True
            user= token.user
            token.delete()
            token = self.get_model().objects.create(user = user)

        return is_expire, token

    #metodo de autentticacion por token

    def authenticate_credentials(self,key):
        message, token, user = None, None, None

        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user

        except self.get_model().DoesNotExist:
            message = 'Token inválido.'
            self.expired= True
            
            

        if token is not None:
            if not token.user.is_active:
                message = 'usuario no activo o eliminado'
            
        if token is not None:
            is_expired = self.token_expired_handler(token)

            if is_expired:
                message = 'su token a expirado.'
                

        return (user, token, message, self.expired)