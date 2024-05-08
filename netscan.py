#!/usr/bin/env python

import subprocess

while(1):
    print("\n(1) Normal scan \n(2) TCP syn scan\n(3) TCP connect scan\n(4) UDP scan\n(5) service version scan \n(6) Idle scan\n(7) Ping scan\n(8) Host List\n(9) firewall by\n(0) Exit\n")
    type = int(input("Enter the number: "))
    if type == 1:
        ip = input("Enter the ip: ")
        pt = input("Port specification ?(y/n): ")
        if pt == "y":
            ty2 = int(input("\n(1) Spcific ports\n(2) All ports\n(3) Top ports\nEnter the number: "))
            if ty2 == 1:
                ptn = input("enter the port number: ")
                subprocess.call("nmap " + ip + " -p " + ptn, shell=True)
            elif ty2 == 2:
                subprocess.call("nmap " + ip + " -p-", shell=True)
            elif ty2 == 3:
                top = int(input("\n(1) Top 100\n(2) Top 200\n(3) Custom\n"))
                if top == 1:
                    subprocess.call("nmap " + ip + " --top-ports 100", shell=True)
                elif top == 2:
                    subprocess.call("nmap " + ip + " --top-ports 200", shell=True)
                elif top == 3:
                    ptt = input("Enter port count: ")
                    subprocess.call("nmap " + ip + " --top-ports " + ptt, shell=True)
        else:
            subprocess.call("nmap " + ip, shell=True)dd
