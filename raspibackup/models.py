from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=255, primary_key=True)
    backup_root_dir = models.CharField(max_length=255)
    remote_backup_dir = models.CharField(max_length=255)
    remote_user = models.CharField(max_length=255)
    remote_host = models.CharField(max_length=255)
    
class Backup(models.Model):
    backup_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client)
    backup_start_time = models.DateTimeField(null=False)
    backup_end_time = models.DateTimeField(null=True)
    backup_path = models.CharField(max_length=255, null=True)
    
