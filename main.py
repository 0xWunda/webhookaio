import csv
import sys
import time
from os import system, name
import requests
import colorama
import pyfiglet
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from colorama import Fore, Style, Back
colorama.init(autoreset=True)


def main():
   menu()


def menu():
    system('cls')
    print(Fore.LIGHTCYAN_EX + "************Webhook tools by Beezyboy**************")
    print()
    print("1.  Webhook Deleter")
    print("2.  Webhook Spammer")
    print("3.  Exit")
    choice = input("Please enter your choice: ")

    if choice == "1":
        deleter()

    elif choice == "2":
        spammer()

    elif choice=="3":
        sys.exit
        
    else:
        system('cls')
        print("Select 1,2 or 3!")
        print(Fore.RED + "Try Again!")
        print()
        time.sleep(2)
        menu()



def deleter():
    webhook = input("Webhook URL: ")

    try:
        r = requests.get(webhook, verify=False)

    except:
        print("Invalid URL")
        sys.exit(1)

    if(r.status_code==200):
        print("Webhook Online")

    else:
        print("Webhook Offline")
        sys.exit(1)
    
    requests.delete(webhook)

    r = requests.get(webhook, verify=False)
    if(r.status_code==404):
        print(Fore.GREEN + "Deleted!")

    else:
        print(Fore.RED + "Failed To Delete")





def spammer():
    msg = input("Please Insert WebHook Spam Message: ")
    webhook = input("Please Insert WebHook URL: ")
    def spam(msg, webhook):
        while True:
            try:
                data = requests.post(webhook, json={'content': msg})
                if data.status_code == 204:
                    print(f"Sent MSG {msg}")
            except:
                print("Bad Webhook :" + webhook)
                time.sleep(5)
                exit()
    kingman_top = 1
    while kingman_top == 1:
        spam(msg, webhook)
    

main()