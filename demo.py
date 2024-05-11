#!/usr/bin/env python

import subprocess

def port():
    ty2 = int(input("\n(1) Spcific ports\n(2) All ports\n(3) Top ports\nEnter the number: "))
    if ty2 == 1:
        ptn = input("enter the port number: ")
        return " -p "+ptn
    elif ty2 == 2:
        return " -p-"
    elif ty2 == 3:
        top = int(input("\n(1) Top 100\n(2) Top 200\n(3) Custom\n"))
        if top == 1:
            return " --top-ports 100"
        elif top == 2:
            return " --top-ports 200"
        elif top == 3:
            ptt = input("Enter port count: ")
            return " --top-ports "+ptt
while(1):
    print("\n(1) Normal scan \n(2) TCP syn scan\n(3) TCP connect scan\n(4) UDP scan\n(5) service version scan \n(6) Idle scan\n(7) Ping scan\n(8) Host List\n(9) firewall by\n(0) Exit\n")
    type = int(input("Enter the number: "))
    if type == 0:
        exit()
    elif type >9:
        print("Invalid input")
    else:
        ip = input("Enter the ip: ")
        pt = input("Port specification ?(y/n): ")
        if pt == "y" or pt == "Y":
            ptype = port()
            if type == 1:
                subprocess.call("nmap " + ip + ptype, shell=True)
            elif type == 2:
                subprocess.call("nmap -sS " + ip + ptype, shell=True)
            elif type == 3:
                subprocess.call("nmap -sT " + ip + ptype, shell=True)
            elif type == 4:
                subprocess.call("nmap -sU " + ip + ptype, shell=True)
            elif type == 5:
                subprocess.call("nmap -sV -O " + ip + ptype, shell=True)
            elif type == 6:
                subprocess.call("nmap -sI " + ip + ptype, shell=True)
            elif type == 7:
                subprocess.call("nmap -sP " + ip + ptype, shell=True)
            elif type == 8:
                subprocess.call("nmap -sL " + ip + ptype, shell=True)
            elif type == 9:
                subprocess.call("nmap -Pn " + ip + ptype, shell=True)

        elif pt == "n" or pt == "N":
            if type == 1:
                subprocess.call("nmap " + ip, shell=True)
            elif type == 2:
                subprocess.call("nmap -sS " + ip, shell=True)
            elif type == 3:
                subprocess.call("nmap -sT " + ip, shell=True)
            elif type == 4:
                subprocess.call("nmap -sU " + ip, shell=True)
            elif type == 5:
                subprocess.call("nmap -sV -O " + ip, shell=True)
            elif type == 6:
                subprocess.call("nmap -sI " + ip, shell=True)
            elif type == 7:
                subprocess.call("nmap -sP " + ip, shell=True)
            elif type == 8:
                subprocess.call("nmap -sL " + ip, shell=True)
            elif type == 9:
                subprocess.call("nmap -Pn " + ip, shell=True)
