from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 5000
min_port = 1

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
    print('[*] Benvenuto sullo scanner di porte')
    host = raw_input('[*] Inserisci target: ')
except KeyboardInterrupt:
    print('\n\n[*] Utente ha richiesto un interruzione')
    print('\n[*] Applicazione si sta chiudendo')
    sys.exit(1)
hostip = gethostbyname(host)
print('\n[*] Host: %s IP: %s' % (host ,hostip))
print('[*] Scan partito alle %s... \n' % (time.strftime('%H:%M:%S')))
start_time = datetime.now()

for port in range(min_port , max_port):
    try:
        response = scan_host(host, port)
        if response == 0:
            print('[*] Porta %s aperta..' % (port))
    except Exception, e:
        pass
stop_time = datetime.now()
time_duration = stop_time - start_time
print('\n[*] Scan finito alle %s...' % (time.strftime('%H:%M:%S')))
print('[*] Scan durato: %s ' % (time_duration))
print('[*] Abbi una bella giornata!')
