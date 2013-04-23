from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project2.views.home', name='home'),
    url(r'^login/$', 'project2.views.login', name='login'),
    url(r'^search/', include('search.urls', namespace = "search") ),
    url(r'^favorites/', include('favorites.urls', namespace = "favorites") ),
    url(r'^admin/', include(admin.site.urls)),
    
   # url(r'^login/$', 'django.contrib.auth.views.login'),
   # url(r'^logout/$', 'logout_page'),
 
    # Examples:
    # url(r'^$', 'project2.views.home', name='home'),
    # url(r'^project2/', include('project2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
