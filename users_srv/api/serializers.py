from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализация данных о пользователе в json
    """
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'last_login',
            'is_superuser',
            'password',
        ]
        extra_kwargs = {
            'security_question': {'write_only': True},
            'security_question_answer': {'write_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
