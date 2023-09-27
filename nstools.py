#!/usr/bin/python3


import os
import time
import getpass
import subprocess
import psutil


def system_report() -> None:

    print_header("System Report")
    get_mounts_info()
    get_resources_info()

    print("\n\n\t\tPress any key to back main menu\n\n")
    input()


def get_mounts_info() -> None:

    
    cmd = "mount -v |grep -v 'docker' |grep '/dev/' |awk '{print $3}'"
    result,code = RunCommand(cmd)

    mounts = result.split("\n")
    print(f"\t\t##################### PARTITIONS ##########################\n\n")
    for mount in mounts:
        a = RunCommand(f"df -h {mount}")
        print(a[0] + "\n")


def get_resources_info() -> None:

    print(f"\t\t##################### RESOURSES ##########################\n\n")
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load15/os.cpu_count()) * 100
 
    print("The CPU usage is : ", round(cpu_usage,2))
    print('RAM memory % used:', psutil.virtual_memory()[2])





def readfile(file:str) -> list:

    '''
        lee un archivo de texto y mete en una lista linea por linea
    '''
    lines = []
    # Using readline()
    file1 = open(file, 'r')
    count = 0
    while True:
        count += 1
 
        # Get next line from file
        line = file1.readline()
 
        # if line is empty
        # end of file is reached
        if not line:
            break
        lines.append(line)
 
    file1.close()
    return lines


def wipe_logs() -> None:
    '''
        Borrar logs archivados y limpia logs actuales  
    
    '''
    files = [ '/var/log/asterisk/messages',
             '/var/log/asterisk/full',
             '/var/log/asterisk/issabelpbx.log',
             '/var/log/asterisk/queue_log',
             '/var/log/asterisk/issabelpbx_dbug',
             '/opt/issabel/dialer/dialerd.log',
             '/var/log/fail2ban.log'

             ]
    
    deep_files = ['/var/log/asterisk/cdr-csv/Master.csv',
                  ]
    
    patters = ['/var/log/asterisk/full-*',
               '/var/log/asterisk/messages-*',
               '/opt/issabel/dialer/dialerd.log-*',
               '/var/log/fail2ban.log-*',
               '/var/log/boot.log-*',
               '/var/log/cron-*',
               '/var/log/maillog-*',
               '/var/log/messages-*',
               '/var/log/secure-*',
               '/var/log/spooler-*',
               '/var/log/yum.log-*']


    print_header("Wipe Logs")
    text = f"\t\tDo you want to wipe logs? Y(Yes) | N(No) | A(All)\n\n"
    print(text)
    opt =  input()

    if opt.upper() == "Y" or opt.upper() == "A":
        #Limpia los archivos
        for file in files:
            RunCommand(f"truncate -s 0 {file}")

        #Borra archivados
        for patter in patters:
            RunCommand(f"rm -f {patter}")

        if opt.upper() == "A":
            #Borra archivos opcionales
            for deep_file in deep_files:
                RunCommand(f"truncate -s 0 {deep_file}")




def delete_recordings() -> None:


    print_header("Delete Recordings")

    text = f"\t\tEnter number of days to delete or B for back to main menu\n\n"
    print(text)
    opt = input()

    if opt.upper() != "B":

        
        cmd = f"find /var/spool/asterisk/monitor -type f -mtime +{opt} |wc -l"

        result,code = RunCommand(cmd)

        print (f"\t\tAre you sure delete {result} files?  Y / N \n\n")
        conf = input()
        if conf.upper() == "Y":
            cmd2 = f"find /var/spool/asterisk/monitor -type f -mtime +{opt} -delete"
            RunCommand(cmd2)

  
def RunCommand(pcmd:str) -> str:
    '''
        Ejecuta un comando y devuelve la salida y codigo
    '''
    output_raw = subprocess.Popen(pcmd,stdout=subprocess.PIPE,shell=True)
    output_code = output_raw.wait()
    output_result,err = output_raw.communicate()
    a = output_result.decode('utf-8')
    output = a.strip()
    return output,output_code




def create_file(file_name:str, text:str) -> bool:
    '''
        Crea un archivo de texto con el contenido que se le ha pasado 
    '''

    f = open(file_name, "w")
    f.write(text)
    f.close()

    if os.path.isfile(file_name):
        return True
    else:
        return False



def check_file(file_name:str) -> bool:

    '''
        Check if file exist 
    '''

    return os.path.isfile(file_name)


def recycle_recordings() -> None :

    '''
        Check for recording recycle cron job
    '''
    file_name = "/etc/cron.d/nspbx_recordings"
    
    os.system('clear')
    print_header("Enable/Disable Recording recycle")
    if check_file(file_name):
        
        with open(file_name) as f:
            first_line = f.readline().strip('\n')
        
        arry_line = first_line.split() 
        

        text = f"\t\tSTATUS: ACTIVE FOR {arry_line[11]} DAYS\n\n\
        \tEnter D to disable or any key for back main menu\n\n"

        print(text)

        dis = input()

        if dis.upper() == "D":
            os.remove(file_name)
         

    else:
        
        text = "\t\tSTATUS: NO ACTIVE\n\n\
        \tEnter days to keep or B for back main menu\n\n"
        
        
        print(text)
        
        days = input()

        if days.upper() == "B":
            pass
        else:
            file_text = f"30 11 * * * root find /var/spool/asterisk/monitor -type f -mtime +{days} -delete\n"
            create_file(file_name,file_text)


def print_header(name: str) -> None:

    '''
        Header printing
    
    '''

    os.system('clear')
    header="\t\t###########################################################\n\
                #                                                         #\n\
                #           NSTOOLS  v0.2                                 #\n\
                #                      Christopher Naranjo G.             #\n\
                #                         <cnaranjo@nsoporte.com>         #\n\
                #                                                         #\n\
                ###########################################################\n\
                "
    

    print (header)
    print ("\t\t\t\t" + name + "\n")





def print_main_menu() -> None:

    '''

        Imprime un menu con las opciones a seleccionar
    
    '''
    os.system('clear')
    print_header("Main Menu")
    menu_str =      "\
                    \t\t1- Enable/Disable Recording recycle\n\
                    \t\t2- Delete Recordings by time\n\
                    \t\t3- Wipe Logs\n\
                    \t\t4- System Report\n\n\
                    \t\tQ- Quit\n\n\n\
                    Please Select an Option:\n" 
    
    
    
    
    
    print(menu_str)
    opt = input()

    if opt == "1":
        recycle_recordings()

    elif opt == "2":
        delete_recordings()    

    elif opt == "3":
        wipe_logs()

    elif opt == "4":
        system_report()

    elif opt.upper() == "Q":
        
        exit()    


    else:
        print("Invalid Option")
        time.sleep(1.0)



if __name__ == '__main__':
    
    
    if getpass.getuser() == "root":
        while True:
            print_main_menu()
    
    else:
        print ("ERROR: NSTOOLS must run as root user")


    