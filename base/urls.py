from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'/$', views.Instructors.as_view(), name='instructors'),
    url(r'instructors/(?P<pk>[0-9]+)/$', views.InstructorsDetail.as_view()),
    url(r'users/$', views.Users.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
