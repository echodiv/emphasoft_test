from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView, DetailView

from django.contrib.auth.models import User

from .forms import NewAccountForm


class UserListView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        """
        Отображение всех аккаунтов заведенных в системе
        """
        all_accounts = User.objects.all()
        paginator = Paginator(all_accounts, 10)
        page = request.GET.get('page') or 1

        try:
            accounts = paginator.page(page)
        except PageNotAnInteger:
            accounts = paginator.page(1)
        except EmptyPage:
            accounts = paginator.page(paginator.num_pages)
        return render(request, 'accounts/list.html',
                      {
                          'accounts': accounts,
                          'page': page,
                      })


class AccountManageView(LoginRequiredMixin, View):
    """
    Заведение нового аккаунта в систему
    """
    @staticmethod
    def get(request):
        """
        Отображение формы заведения аккаунта
        """
        form = NewAccountForm
        return render(request, 'accounts/create.html', {'form': form})

    @staticmethod
    def post(request):
        """
        Обработка запроса на заведение нового аккаунта
        """
        form = NewAccountForm(request.POST)
        if form.is_valid():
            new_account = form.save(commit=True)
            flash = f'Account {new_account.username} successful created'
            new_form = NewAccountForm
            return render(request, 'accounts/create.html',
                          {'form': new_form, 'flash': flash})
        else:
            return render(request, 'accounts/create.html',
                          {'form': form, 'flash': form.errors})


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    """
    Удаление пользователя из системы
    """
    model = User
    success_url = reverse_lazy('accounts:accounts_list')


class UpdateAccountView(LoginRequiredMixin, UpdateView):
    """
    Обновление информации об аккаунте пользователя
    """
    model = User
    template_name = "accounts/update.html"
    success_url = reverse_lazy('accounts:accounts_list')
    fields = [
        'username',
        'last_name',
        'first_name',
        'password',
        'email',
        'is_active',
        'is_superuser'
    ]

    def form_valid(self, form):
        """
        Необходима для правильной обработки пароля
        """
        password = form.cleaned_data.get('password')
        if not password:
            return super().form_valid(form)

        self.object.set_password(password)
        return super().form_valid(form)


class AccountDetailView(LoginRequiredMixin, DetailView):
    """
    Детальная информация о пользователе
    """
    model = User
    template_name = "accounts/detail.html"
    fields = [
        'username',
        'last_name',
        'first_name',
        'email',
        'is_active',
        'is_superuser'
    ]
