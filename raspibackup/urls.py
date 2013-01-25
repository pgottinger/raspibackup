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
     url(r'^raspibackup/newbackup/', 'raspibackup.views.new_backup'),
     url(r'^raspibackup/backups/', 'raspibackup.views.backups_overview'),
     url(r'^raspibackup/deletebackup/', 'raspibackup.views.delete_backup'),
     url(r'^raspibackup/show_log/', 'raspibackup.views.show_log'),
     url(r'^raspibackup/clients/', 'raspibackup.views.clients_overview'),
     url(r'^raspibackup/$', 'raspibackup.views.index'),
)
