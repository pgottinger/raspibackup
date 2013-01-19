from django.http import HttpResponse
from raspibackup.models import Client, Backup
import subprocess
import datetime
from thread import start_new_thread

link_to_latest_backup = "current"
backup_folder_prefix = "backup_"
rsync_command = 'rsync -avz --link-dest='
ssh_command = ' -e ssh '
rm_command = 'rm '
lns_command = 'ln -s '


def backup(request):
    client = request.GET.get('client')
    start_new_thread(do_linux_backup, (client,))

    html = "<html><body>Backup successfully started!</body></html>"
    return HttpResponse(html)    

def do_linux_backup(client_param):
    client = Client.objects.get(client_name = client_param)
    now = datetime.datetime.now()
    
    backup = Backup(client = client, backup_start_time = now)
    backup.save()
    
    timestamp = now.strftime("%Y-%m-%d_%H:%M:%S")
    host_backup_root_dir = client.backup_root_dir + client.client_name + "/"
    host_current_backup_dir = host_backup_root_dir + backup_folder_prefix + timestamp

    subprocess.check_output( rsync_command + host_backup_root_dir + link_to_latest_backup + ssh_command + client.remote_user + '@' + client.remote_host + ':' + client.remote_backup_dir + ' ' + host_current_backup_dir, shell=True)
    subprocess.check_output(rm_command + host_backup_root_dir + link_to_latest_backup, shell=True)
    subprocess.check_output(lns_command  + host_backup_root_dir + backup_folder_prefix + timestamp + ' ' + host_backup_root_dir + link_to_latest_backup, shell=True)
    
    backup.backup_end_time = datetime.datetime.now()
    backup.backup_path = host_current_backup_dir
    backup.save()
        
