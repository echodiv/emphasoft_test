from django.conf.urls import url

from .views import UsersViewSet


app_name = 'api'

urlpatterns = [
       url(r'^users/(?P<pk>[\w]+)/$', UsersViewSet.as_view(
           {
               'get': 'retrieve',
               'put': 'update',
               'patch': 'partial_update',
               'delete': 'destroy',
           }
       ),
           name='user_manage'),
       url(r'^users/$', UsersViewSet.as_view(
           {
               'get': 'list',
               'post': 'create',
           }
       ), name='user_list'),
]
