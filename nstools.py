
import os
import time
import getpass
import subprocess




def delete_recordings() -> None:


    print_header("Delete Recordings")

    text = f"\t\tEnter number of days to delete or B for back to main menu\n\n"
    print(text)
    opt = input()

    #load_file_list(120,"/var/spool/asterisk/monitor")

  
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





def load_file_list(days:int, path:str) -> list:

    '''
        Recibe un entero con los dias que de deben conservar, 
        junto con el path, este devuelve una lista con los archivos
    '''

    cmd = f"find {path} -type f -mtime +{days}"
    result,code = RunCommand(cmd)

    print (result)
    input()








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
                #           NSTOOLS                                       #\n\
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
                    \t\t3- Wipe Logs\n\n\
                    \t\tS- Exit\n\n\n\
                    Please Select an Option:\n" 
    
    
    
    
    
    print(menu_str)
    opt = input()

    if opt == "1":
        recycle_recordings()

    elif opt == "2":
        delete_recordings()    

    elif opt == "3":
        pass

    elif opt.upper() == "S":
        
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


    