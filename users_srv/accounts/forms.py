from django import forms

from django.contrib.auth.models import User


class NewAccountForm(forms.ModelForm):
    """Форма для заведения нового аккаунта в систему
    """
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'password',
            'email',
            'is_active',
            'is_superuser'
        ]
