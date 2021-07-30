from django.conf.urls import url

from .views import UserListView, NewAccountView


app_name = 'accounts'

urlpatterns = [
    url(r'^new_account/$', NewAccountView.as_view(), name='new_account'),
    url(r'^$', UserListView.as_view(), name='accounts_list'),
]
