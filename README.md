raspibackup
===========

raspibackup aims to be a backup tool for the Raspberry Pi based on rsync.

Target is to have a Django-based web application on the Raspberry Pi that is used to manage the backups. 
The clients to backup can be added in the web application. Aftwards you can trigger a backup of a client through 
the web interface.

What is also planned is a REST API for the application to trigger a backup from a client or for regular backups by (e.g.)
a cron job.
