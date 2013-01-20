from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raspibackup.views.home', name='home'),
    # url(r'^raspibackup/', include('raspibackup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^newbackup/', 'raspibackup.views.new_backup'),
     url(r'^backups/', 'raspibackup.views.backups_overview'),
     url(r'^deletebackup/', 'raspibackup.views.delete_backup'),
     url(r'^show_log/', 'raspibackup.views.show_log'),
     url(r'^clients/', 'raspibackup.views.clients_overview'),
     url(r'^$', 'raspibackup.views.index'),
)
