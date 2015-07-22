# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

__author__ = 'joanbiscarri'

from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()    # read only
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instacia de user a partir de los datos de validated_data que contiene valores deserializados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto User
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de los datos del diccionario validated_data que contiene valores deserializados
        :param instance: user a  actualizar
        :param validated_data:  diccionario de nuevos valores para el user
        :return: objeto user actualizado
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))   # encripto contrasena
        instance.save()
        return instance

    # validacion en un serializer, para el campo username (el nombre del metodo debe tener este formato)
    def validate_username(self, data):
        """
        Valida si existe un user con ese username. Incluso si hago un update, se hara la comprobacion
        """
        # Si estoy creando (no hay instancia) compruebo si hay usuarios con ese username
        # Si estoy updatando, y quiero cambiar mi username, nombre distinto en instancia y el que pongo ,y existe algun user con ese nombre: error
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError('Existing user, insert not allowed')
        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError('Existing user, update not allowed')
        else:
            return data

class BlogSerializer(serializers.Serializer):
    username = serializers.CharField()