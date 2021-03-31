
from django.db.models import fields
from rest_framework import serializers
from users.models import User

#un serializador es un modelo pero en formato Json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

       


# serializador para listar

class UserListserializer(serializers.ModelSerializer):
    class Meta:
        model = User

# Metodo que llama la automatizacion que toma los campos especificados en fields.
# Este metodo se usa cuando se quiere listar varios objetos.

    def to_representation(self,instance):

        # se usa como diccionario si en la consulta se usa la propiedad values()
        #si no se usa se trata como objeto, con .

        return {'id':instance['id'],
        'username':instance['username'],
        'email':instance['email'],
        'password':instance['password']
        }

# serializador para tokens

class UserTokenserializador(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=('username','email')
       
        




