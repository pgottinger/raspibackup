from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^raspibackup/newbackup/', 'raspibackup.views.new_backup'),
     url(r'^raspibackup/backups/', 'raspibackup.views.backups_overview'),
     url(r'^raspibackup/deletebackup/', 'raspibackup.views.delete_backup'),
     url(r'^raspibackup/show_log/', 'raspibackup.views.show_log'),
     url(r'^raspibackup/clients/', 'raspibackup.views.clients_overview'),
     url(r'^raspibackup/$', 'raspibackup.views.index'),
)
