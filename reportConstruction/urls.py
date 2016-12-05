from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
# from .serializer import UserSerializer

urlpatterns = [
	url(r'^report/$', views.ReportConstructionList.as_view()),
	url(r'^report/(?P<pk>[0-9]+)/$', views.ReportConstructionDetail.as_view()),

	# url(r'^users/$', views.UserList.as_view()),
	# url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

	url(r'^$', views.map_api, name='map_api'),
]