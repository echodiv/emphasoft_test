from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views import View

from django.contrib.auth.models import User


class UserListView(View):
    @staticmethod
    def get(request):
        all_accounts = User.objects.all()
        paginator = Paginator(all_accounts, 10)
        page = request.GET.get('page')

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

    @staticmethod
    def post(request):
        pass

