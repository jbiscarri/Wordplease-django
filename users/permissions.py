# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

__author__ = 'joanbiscarri'


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene permiso para realizar la accion: GET, POST, PUT, DELETE
        :param request:
        :param view:
        :return:
        """
        from users.api import UserDetailAPI # Lo importo aqui para evitar dependencias ciclicas
        # si se crea un usuario, todos pueden
        if request.method == 'POST':
            return True
        # Si no es post, el super user siempre puede
        elif request.user.is_superuser:
            return True
        # Si es un get a la vista de detalle, tomo la decision de object_permissions
        elif isinstance(view, UserDetailAPI):
            return True
        else:
            # GET /api/1.0/users
            return False


    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado tiene permiso para realizar la accion (GET, POST, PUT, DELETE) sobre el objeto obj
        :param request:
        :param view:
        :param obj:
        :return:
        """

        #si es superadmin o el usuario autenticado intentahacer GET, PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user == obj
