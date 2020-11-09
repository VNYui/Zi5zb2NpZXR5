import time
import progressbar
import nmap3
import itertools
from nested_lookup import nested_lookup
from rich.console import Console
import manager


def scan_top(h):
    global nm
    global s1
    bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    for i in bar(range(100)):
        s1 = nm.scan_top_ports('{}'.format(h))
        time.sleep(0.2)
    parse_top(s1)
    return s1

def scan_dns(h):
    global nm
    global s2
    bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()

    s2 = nm.nmap_dns_brute_script(f'{h}')

    parse_dns(s2)
    return s2

def scan_list(h):
    global nm
    global s3
    bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    for i in bar(range(100)):
        s3 = nm.nmap_list_scan('{}'.format(h))
        time.sleep(0.5)
    return s3

def scan_os(h):
    global nm
    global s4
    bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    for i in bar(range(100)):
        s4 = nm.nmap_os_detection('{}'.format(h))
        time.sleep(0.5)
    return s4

def scan_subnet(h):
    global nm
    global s5
    bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    for i in bar(range(100)):
        s5 = nm.nmap_subnet_scan('{}'.format(h))
        time.sleep(0.5)
    return s5

def scan_vers(h):
    global nm
    global s6
    bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    for i in bar(range(100)):
        s6 = nm.nmap_version_detection('{}'.format(host))
        time.sleep(0.5)
    return s6

def parse_top(s1):
    global console
    #init console log
    console = Console()
    #RETRIEVE KEY FROM NESTED DICT
    hosts = nested_lookup('host', s1)
    portid = nested_lookup('portid', s1)
    state = nested_lookup('state', s1)
    protocol = nested_lookup('protocol', s1)
    service = nested_lookup('service', s1)
    reason = nested_lookup('reason', s1)
    console.print(f"TOP PORTS SCAN : {hosts[1]}", style="bold red")
    #PARSING PORT / STATE / PROTO / SERVICES / REASON
    for (p,s,proto, serv, res) in zip(portid, state, protocol, service,reason):
        console.print(f"{p} : {s} : {proto} : {serv['name']} : {res}")
    return p,s,proto,serv,res

def parse_dns(s2):
    console.print('Brute Forcing dns..')
    dns_bruted = nested_lookup('address', s2)
    bruted_hostname = nested_lookup('hostname', s2)
    console.print(f"{dns_bruted[1]} : {bruted_hostname[1]}")

"""def debug():
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)"""

def main(h):
    global console
    console = Console()
    scan_top(h)
    scan_dns(h)
    """scan_list(h)
    scan_os(h)
    scan_subnet(h)
    scan_vers(h)"""
    manager.create(s1,s2)
    #debug()
if __name__ == '__main__':
    main()
