#!/usr/bin/env python3
# Author: Piero Toffanin
# License: AGPLv3

import os
import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description='Utility to ping hosts and check for network issues ')
parser.add_argument('--hosts',
                type=str,
                default="hosts.txt",
                help='Path to file with list of hosts to check (.txt)')
parser.add_argument('--retries',
                type=int,
                default=10,
                help='Number of retries before erroring out')

args = parser.parse_args()

with open(args.hosts, 'r') as f:
    hosts = [h.strip() for h in f.read().split() if h.strip() != '']

for host in hosts:
    online = False
    for i in range(args.retries):
        try:
            subprocess.run(['ping', '-c', '1', host], check=True, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
            online = True
            break
        except:
            time.sleep(1 * i)
    if not online:
        print(host + " is not responding")

