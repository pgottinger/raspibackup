from django.db import models

# Create your models here.
class Client(models.Model):
    host = models.CharField(max_length=255, primary_key=True)
    backup_root_dir = models.CharField(max_length=255)
    remote_backup_dir = models.CharField(max_length=255)
    remote_user = models.CharField(max_length=255)
    remote_host = models.CharField(max_length=255)
