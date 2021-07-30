from django.conf.urls import url

from .views import UserListView


app_name = 'accounts'

urlpatterns = [
    url(r'^$', UserListView.as_view(), name='accounts_list'),
]
