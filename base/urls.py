from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import communityPartnerViews
from . import projectViews

urlpatterns = [
    #url(r'/$', views.Instructors.as_view(), name='instructors'),
    #url(r'instructors/(?P<pk>[0-9]+)/$', views.InstructorsDetail.as_view()),
    #url(r'users/$', views.Users.as_view()),
    #url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'communityPartner/$', communityPartnerViews.CommunityPartnerDetail.as_view()),
    url(r'communityPartner/(?P<pk>[0-9]+)/$', communityPartnerViews.CommunityPartnerDetail.as_view()),
    url(r'communityPartner/(?P<pk>[0-9]+)/projects/$', communityPartnerViews.CommunityPartnerProjects.as_view()),
    url(r'project/$', projectViews.ProjectDetail.as_view()),
    url(r'project/(?P<pk>[0-9]+)/$', projectViews.ProjectDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
