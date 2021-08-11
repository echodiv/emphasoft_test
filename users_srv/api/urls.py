from django.conf.urls import url

from .views import UsersListViewSet, UserDetailViewSet


app_name = 'api'

urlpatterns = [
       url(r'^users/(?P<pk>[\w]+)/$', UserDetailViewSet.as_view(
           {
               'get': 'retrieve',
               'put': 'update',
               'patch': 'partial_update',
               'delete': 'destroy',
           }
       ),
           name='user_manage'),
       url(r'^users/$', UsersListViewSet.as_view(
           {
               'get': 'list',
               'post': 'create',
           }
       ), name='user_list'),
]
