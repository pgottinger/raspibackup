from django.shortcuts import render_to_response
from raspibackup.models import Client, Backup
from raspibackup.backup import do_linux_backup, delete_backup_id, read_log_file
from thread import start_new_thread

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
    backup_id = request.GET.get('backup_id')
    backup = Backup.objects.get(backup_id = backup_id)
    file_content = read_log_file(backup)
    context = {
               'file_content': file_content,
               'backup': backup,
               }
    
    return render_to_response('show_log.html', context)


def new_backup(request):
    client_param = request.GET.get('client')
    client = Client.objects.get(client_name=client_param)
    threaded_param = request.GET.get('threaded')
    
    if threaded_param == "false":
        do_linux_backup(client)    
    else:
        start_new_thread(do_linux_backup, (client,))
    return render_to_response('newbackup.html')    

def delete_backup(request):
    backup_id = request.GET.get('backup_id')
    delete_backup_id(backup_id)
    
    context = {
               'backup_id': backup_id,
               }
    return render_to_response('backup_deleted.html', context)
        
