from django.http import HttpResponse
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
    host = request.GET.get('host')
    backup_root_dir = request.GET.get('backup_root_dir')
    remote_backup_dir = request.GET.get('remote_backup_dir')
    remote_user = request.GET.get('remote_user')
    remote_host = request.GET.get('remote_host')

    start_new_thread(do_linux_backup, (backup_root_dir, host, remote_backup_dir, remote_user, remote_host,))
    html = "<html><body>Backup successfully started!</body></html>"
    return HttpResponse(html)    

def do_linux_backup(backup_root_dir, host, remote_backup_dir, remote_user, remote_host):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H:%M:%S")
    host_backup_root_dir = backup_root_dir + host + "/"

    subprocess.check_output( rsync_command + host_backup_root_dir + link_to_latest_backup + ssh_command + remote_user + '@' + remote_host + ':' + remote_backup_dir + ' ' + host_backup_root_dir + backup_folder_prefix + timestamp, shell=True)
    subprocess.check_output(rm_command + host_backup_root_dir + link_to_latest_backup, shell=True)
    subprocess.check_output(lns_command  + host_backup_root_dir + backup_folder_prefix + timestamp + ' ' + host_backup_root_dir + link_to_latest_backup, shell=True)
        
