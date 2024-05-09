#!/usr/bin/env python

import subprocess


def port():
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


while (1):
    print(
        "\n(1) Normal scan \n(2) TCP syn scan\n(3) TCP connect scan\n(4) UDP scan\n(5) service version scan \n(6) Idle scan\n(7) Ping scan\n(8) Host List\n(9) firewall by\n(0) Exit\n")
    type = int(input("Enter the number: "))
    ip = input("Enter the ip: ")
    if type == 1:
        pt = input("Port specification ?(y/n): ")
        if pt == "y" or pt == "Y":
            port()
        else:
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
    elif type == 0:
        exit()
    else:
        print("Invalid input")
    op = input("Want to save output(Y/N): ")
    if op == "y" or op == "Y":


