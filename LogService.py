import os
from os.path import join
import datetime

def save_log(cedula,errorCode,path):

    date = datetime.datetime.now()
    current_path = os.getcwd()
    file_path = join(current_path,'log')
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    file_path_log = join(file_path,path)
    if not os.path.isdir(file_path_log):
        os.mkdir(file_path_log)
    log = f'{cedula} // evento  // \'{errorCode}\'' if path == 'database' else  f'{errorCode}-{date.strftime("%d%m%Y")}'
    print(log)
    print(f'log-{date.strftime("%d%m%Y")}')
    # with open(join(file_path_log,f'logs-{cedula}-{date.strftime("%d%m%y%H%M")}.txt'), 'wt') as f:
                # f.write(log)
    with open(join(file_path_log,f'log-{cedula}.txt'), 'at') as f:
                f.write(log + '\n')


def save_log_error(errorcode:str,path:str,cedula:str = '') -> str:

    date= datetime.datetime.now()
    path_complete = join(path,f'{cedula}_error.txt')
    f = open(path_complete,'wt')
    f.write(errorcode)
    return "File save successfully"


   


