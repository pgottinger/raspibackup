import subprocess
import datetime
from django.shortcuts import render_to_response
from raspibackup.models import Client, Backup
from thread import start_new_thread
from subprocess import CalledProcessError

link_to_latest_backup = "current"
backup_folder_prefix = "backup_"
backup_log_filename = "backup.log"
rsync_command = "rsync -avz --stats --link-dest="
ssh_command = " -e ssh "
rm_command = "rm "
lns_command = "ln -s "
mkdir_command = "mkdir "


def index(request):
    return render_to_response('index.html')

def backups_overview(request):
    context = {    
               'backups': Backup.objects.all(),
    }
    return render_to_response('backups_overview.html', context)    

def clients_overview(request):
    context = {    
               'clients': Client.objects.all(),
    }
    return render_to_response('clients_overview.html', context)  

def show_log(request):
    backup_id = request.GET.get('backup_id');
    backup = Backup.objects.get(backup_id = backup_id)
    f = open(backup.backup_log_path, 'r')
    file_content = []

    for line in f:
        file_content.append(line)
    
    f.close()
    context = {
               'file_content': file_content,
               'backup': backup,
               }
    
    return render_to_response('show_log.html', context)


def new_backup(request):
    client_param = request.GET.get('client')
    client = Client.objects.get(client_name=client_param)
    start_new_thread(do_linux_backup, (client,))
        
    
    return render_to_response('newbackup.html')    

def do_linux_backup(client):
    now = datetime.datetime.now()
    
    backup = Backup(client=client, backup_start_time=now)
    backup.save()
    
    timestamp = now.strftime("%Y-%m-%d_%H:%M:%S")
    host_backup_root_dir = client.backup_root_dir + client.client_name + "/"
    host_current_backup_dir = host_backup_root_dir + backup_folder_prefix + timestamp
    
    rsync_backup_command = rsync_command + host_backup_root_dir + link_to_latest_backup + ssh_command + client.remote_user + '@' + client.remote_host + ':' + client.remote_backup_dir + ' ' + host_current_backup_dir
    backup_file_path = host_current_backup_dir + '/'+ backup_log_filename
    backup_log_command = ' >> ' + backup_file_path +' 2>&1' 

    # creating folder and and printing backup command to the log file
    try:
        subprocess.check_output(mkdir_command + host_current_backup_dir, shell=True)
        subprocess.check_output("echo 'rsync-command:" + rsync_backup_command +"\n\n'"+ backup_log_command, shell=True)
        
        backup.backup_path = host_current_backup_dir
        backup.backup_log_path = backup_file_path
        backup.save()
    
        # do the backup and the linking
        subprocess.check_output(rsync_backup_command + backup_log_command, shell=True)
        subprocess.check_output(rm_command + host_backup_root_dir + link_to_latest_backup + backup_log_command, shell=True)
        subprocess.check_output(lns_command + host_backup_root_dir + backup_folder_prefix + timestamp + ' ' + host_backup_root_dir + link_to_latest_backup + backup_log_command, shell=True)
        backup.backup_successful = True
    except CalledProcessError:
        backup.backup_successful = False
        
    # write the back end time to the database to show that the backup is finished 
    backup.backup_end_time = datetime.datetime.now()
    backup.save()

def delete_backup(request):
    backup_id = request.GET.get('backup_id');
    backup = Backup.objects.get(backup_id = backup_id)
    subprocess.check_output('rm -rf '+backup.backup_path, shell=True)
    
    backup.delete()
    
    context = {
               'backup_id': backup_id,
               }
    return render_to_response('backup_deleted.html', context)
        
