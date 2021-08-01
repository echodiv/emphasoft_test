from django.conf.urls import url

from .views import UsersListView, UsersDetailView


app_name = 'api'

urlpatterns = [
       url(r'^users/(?P<pk>[\w]+)/$', UsersDetailView.as_view(),
           name='user_manage'),
       url(r'^users/$', UsersListView.as_view(), name='user_list'),
]
