#!/usr/bin/python3

import os
os.system("figlet NETWORK WIZARD")
option = ["(1.) Scan a specific port","(2.) Os detection","(3.)Nmap service Detection","(4.)Nmap Agressive scan","(5.)Nmap TCP SYN","(6.)Scan using TCP Connect scan"]
for stuffs in option:
    print(stuffs)
choice = input("Enter your choice:")
if choice == "1":
    print("You are currently using nmap normal scan")
    site = input("Enter your target:")
    port = input ("Enter the port number :")
    os.system(" sudo nmap " + site + " -p " + port  )
elif choice == "2":
    print("You are currently using Nmap Os detection")
    target = input("Enter your target:")
    os.system(" sudo nmap -O " + target)
elif choice == "3":
    print("You are currently using Nmap service Detection")
    service = input("Enter your target:")
    os.system("sudo nmap -sV " + service)
elif choice == "4":
    print("You are currently using Nmap aggressive scan")
    aggressive = input("Enter your target:")
    os.system("sudo nmap -A " + aggressive)
elif choice == "5":
    print("You are currently using Nmap TCP SYN")
    TCP = input("Enter your target:")
    os.system("sudo nmap  -sS  " + TCP)
elif choice == "6":
    print("You are currently using Scan using TCP Connect scan")   
    TCP_connect = input("Enter your target:")
    os.system ("sudo nmap -sT " + TCP_connect)
else:
    print("INVALID INPUT !!!!!")
     



