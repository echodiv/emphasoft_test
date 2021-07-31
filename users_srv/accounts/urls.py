from django.conf.urls import url

from .views import UserListView, AccountManageView, DeleteAccountView


app_name = 'accounts'

urlpatterns = [
    url(r'accounts_manage/(?P<pk>[\w]+)/delete/$', DeleteAccountView.as_view(),
        name='account_delete'),
    url(r'^account_manage/$', AccountManageView.as_view(),
        name='account_manage'),
    url(r'^$', UserListView.as_view(), name='accounts_list'),
]
