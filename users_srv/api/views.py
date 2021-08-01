from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer


class UsersListView(ListAPIView):
    """
    Получение всех пользователей системы
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @staticmethod
    def post(request):
        """
        Создание нового пользователя
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({'errors': serializer.errors})


class UsersDetailView(RetrieveAPIView):
    """
    Получение данных о конкретном пользователе
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def post(self, request, pk):