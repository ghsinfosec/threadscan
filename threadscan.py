#!/usr/bin/env python3

# Threaded port scanner inspired by Threader3000

# I had to implement the threading functionality based on threader3000
# because I got stuck in my implementation and couldn't get figure it out.
# Overall the funcionality is similar, but I took my own approach ultimately
# copying the threader function and using the queue library

# Threader3000 can be found here: https://github.com/dievus/threader3000
# Credit to The Cyber Mentor (TCM) and The Mayor for the inspiration and code implementation
# TCM: https://github.com/hmaverickadams
# The Mayor: https://github.com/dievus

from datetime import datetime
import os
import pyperclip
import socket
import subprocess
import sys
from threading import Thread
from queue import Queue

# define target based on given argument
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid number of arguments.")
    print("Usage: python3 portscanner.py <ip>")

# add banner
print("-" * 70)
print("\tThreaded Port Scanner - Inspired by TCM & The Mayor")
print(f"\tScanning target: {target}")
print("\tStart time: " + str(datetime.now()))
print("-" * 70)
print("\n")

# list to hold the open ports that are discovered
open_ports = []

# scan function to find open ports
def scan_ports(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # returns error indicator
        if result == 0:
            print(f'Port {port} is open')
            open_ports.append(str(port))

# threader function from threader3000
# i need to learn more about threading
def threader():
    while True:
        worker = q.get()
        scan_ports(worker)
        q.task_done()

q = Queue()

# try to connect to the target ports with threading to speed up the scan
try:
    
    # more from threader3000
    for i in range(200):
        t = Thread(target=threader)
        t.daemon = True
        t.start()

    # more from threader3000
    for worker in range(1,65536):
        q.put(worker)

    q.join()

    # suggest an nmap scan for discovered open ports
    print("\nPort scan complete.")
    print("Suggested nmap scan:\n")
    print("nmap -sC -sV -T4 -Pn -p {open_ports} {target} -oN nmap_{target}".format(open_ports=",".join(open_ports), target=target))
    
    # copy the syntax for nmap in case scan is desired
    pyperclip.copy("nmap -sC -sV -T4 -Pn -p {open_ports} {target} -oN nmap_{target}".format(open_ports=",".join(open_ports), target=target))
    
    # check whether a scan is desired
    choice = input("\nRun nmap? [y/n]: ")

    # if scan desired, run it
    if choice == "y":
        runit = pyperclip.paste() # store the command
        os.mkdir("nmap") # make an nmap directory
        os.chdir("nmap") # chdir to store output (-oN nmap_{target})
        subprocess.call("clear", shell=True) 
        print(runit, "\n") # print the command for verification
        subprocess.call(runit, shell=True) # run pasted nmap command
    else:
        sys.exit()

except KeyboardInterrupt:
    print("Keyboard Interrupt. Exiting...")
    sys.exit()

except (socket.gaierror, socket.error) as e:
    print("Error encountered. Exiting...")
    print(e)
    sys.exit()
