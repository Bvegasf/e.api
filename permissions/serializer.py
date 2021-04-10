from django.db import models
from django.db.models import fields
from permissions.models import Permissions, Role
from rest_framework import serializers


class Permissionsserializer(serializers.ModelSerializer):

    class Meta:
        model = Permissions
        fields = '__all__'


class Rolrserializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'