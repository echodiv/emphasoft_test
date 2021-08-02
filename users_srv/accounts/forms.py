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

    def save(self, commit=True):
        """
        Необходима для правильной обработки пароля
        """
        if 'password' in self.cleaned_data:
            self.instance.set_password(self.cleaned_data['password'])
            del self.cleaned_data['password']

        return super().save(commit=commit)
