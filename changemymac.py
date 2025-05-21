#!/usr/bin/env python3
import subprocess
import optparse
import sys

def change(interface, new_mac):
    print(f"[+] Changing MAC address of {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--new_mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

if not options.interface or not options.new_mac:
    print("[-] Error: Please specify both interface and new MAC address.\n")
    parser.print_help()
    sys.exit(1)

change(options.interface, options.new_mac)
