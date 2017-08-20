from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	resume,



	)

urlpatterns = [
	url(r'^posts', post_list, name='list'),
	url(r'^create', post_create, name='crearte_post'),
	url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
	url(r'^resume', resume, name='resume'),


	#url(r'^posts/$', "<appname>.views.<function_name>"),
]
