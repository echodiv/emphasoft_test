from django.conf.urls import url

from .views import (
    UserListView,
    AccountManageView,
    DeleteAccountView,
    UpdateAccountView,
    AccountDetailView,
)


app_name = 'accounts'

urlpatterns = [
    url(r'^accounts_manage/(?P<pk>[\w]+)/update/$',
        UpdateAccountView.as_view(), name='account_update'),
    url(r'^accounts_manage/(?P<pk>[\w]+)/delete/$',
        DeleteAccountView.as_view(), name='account_delete'),
    url(r'^accounts_manage/(?P<pk>[\w]+)/$', AccountDetailView.as_view(),
        name='account_detail'),
    url(r'^account_manage/$', AccountManageView.as_view(),
        name='account_manage'),
    url(r'^$', UserListView.as_view(), name='accounts_list'),
]
