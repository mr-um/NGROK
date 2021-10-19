import os
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN)
print("[+] Downloading Ngrok Please Wait Few Minutes.....")
print()
os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
print("NGROK Downlad Complate.")
os.system(clear)
print("Please wait a couple of second for unzip ngrok...")
os.system("unzip ngrok-stable-linux-arm.zip")
os.system("rm -r ngrok-stable-linux-arm.zip")
print("All Complate")
os.system("clear")