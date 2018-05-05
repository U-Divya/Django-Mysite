from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^$',views.index),			#views.index here index is function written inside views
	url(r'^postform/',views.postform),
]
