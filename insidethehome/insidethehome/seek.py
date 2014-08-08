import datetime
import nmap
import time

import controller

def seek():                         # function to scan the network
    nm = nmap.PortScanner()
    curHosts = []
    nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -T5')
    # executes a ping scan

    localtime = time.asctime(time.localtime(time.time()))
    # system time

    for host in nm.all_hosts():
        try:
            mac = nm[host]['addresses']['mac']
        except:
            mac = 'unknown'

        curHosts.append(mac)

    return curHosts

if __name__ == '__main__':
    while True:
        hosts = seek()

        for host in hosts:
            controller.add_hostname(host, host)
            # device = controller.get_device_by_mac(host)
            # device = controller.santize(device)
            # if device:


