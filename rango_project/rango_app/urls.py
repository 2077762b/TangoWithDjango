from django.conf.urls import patterns, url
from rango_app import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        # url(r'^search/', views.search, name='search'),
	url(r'^goto/', views.track_url, name='goto'),
        url(r'^register_profile/', views.register_profile, name='register_profile'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^view_profile/(?P<profile_name>[\w\-]+)/$', views.view_profile, name='view_profile'),
	url(r'^users/', views.users, name='users'),
	url(r'^restricted/', views.restricted, name='restricted'),)
