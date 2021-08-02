from typing import Union

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpRequest

from .serializers import UserSerializer


class UsersListView(ListAPIView):
    """
    Получение всех пользователей системы
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request: HttpRequest) -> Response:
        """
        Создание нового пользователя
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({'errors': serializer.errors})


class UsersDetailView(APIView):
    serializer_class = UserSerializer

    @staticmethod
    def _check_valid_id(pk: str) -> Union[Response, User]:
        """
        Проверка типа идентификатора и наличия
        пользователя с таким идентификатором
        """
        try:
            int(pk)
            user = User.objects.get(id=pk)
        except ValueError:
            return Response({'error': f'invalid id value'}, status=402)
        except User.DoesNotExist:
            return Response(data='', status=404)
        return user

    def get(self, request: HttpRequest, pk: str) -> Response:
        """
        Получение данных о конкретном пользователе
        """
        user = self._check_valid_id(pk)
        if isinstance(user, Response):
            return user
        serialized_user = self.serializer_class(user)
        return Response(serialized_user.data)

    def put(self, request: HttpRequest, pk: str) -> Response:
        """
        Замена данных о пользователе (если он существует)
        """
        user = self._check_valid_id(pk)
        if isinstance(user, Response):
            return user
        serializer = self.serializer_class(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({'errors': serializer.errors})

    def patch(self, request: HttpRequest, pk: str) -> Response:
        """
        Обновление данных о пользователе
        """
        user = self._check_valid_id(pk)
        if isinstance(user, Response):
            return user
        serializer = self.serializer_class(
            instance=user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({'errors': serializer.errors})

    def delete(self, request: HttpRequest, pk: str) -> Response:
        """
        Удаление пользователя по идентификатору
        """
        if not request.user.is_staff:
            return Response({'error': 'permission denied'}, status=403)

        user = self._check_valid_id(pk)
        if isinstance(user, Response):
            return user

        user.delete()
        return Response(status=204)
