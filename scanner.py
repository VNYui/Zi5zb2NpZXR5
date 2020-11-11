import time
import progressbar
import nmap3
import itertools
import socket
from nested_lookup import nested_lookup
from rich.console import Console
import manager
import threading
import anime
import term
from colorama import init,Fore, Back, Style


def scan_top(h):
    global nm
    global s1
    #bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    #for i in bar(range(100)):
    s1 = nm.scan_top_ports('{}'.format(h))
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
    #bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    #for i in bar(range(100)):
    s4 = nm.nmap_os_detection('{}'.format(h))
    #time.sleep(0.5)
    parse_os(s4)
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

def check_status(s):
    if 'closed' in s:
        s = Fore.RED + 's'
    if 'filterd' in s:
        s = Fore.CYAN + 's'
    else :
        s = Fore.GREEN + 's'
    return s

def parse_top(s1):
    global console
    global hosts
    #init console log
    console = Console()
    #RETRIEVE KEY FROM NESTED DICT
    hosts = nested_lookup('host', s1)
    portid = nested_lookup('portid', s1)
    state = nested_lookup('state', s1)
    protocol = nested_lookup('protocol', s1)
    service = nested_lookup('service', s1)
    reason = nested_lookup('reason', s1)
    #print(f"\nTOP PORTS SCAN : {hosts[1]}")
    #PARSING PORT / STATE / PROTO / SERVICES / REASON

    console.print("\nTOP PORTS SCAN :", style="bold red")
    for (p,s,proto, serv, res) in zip(portid, state, protocol, service,reason):
        #print(f"{p}\t{s}\t{proto}\t{serv['name']}\t{res}".expandtabs(20))
        if 'open' in s :
            a = Fore.GREEN + p + Fore.RESET
            b = Fore.GREEN + s + Fore.RESET
            c = Fore.GREEN + proto + Fore.RESET
            d = Fore.GREEN + serv['name'] + Fore.RESET
            e = Fore.GREEN + res + Fore.RESET
            print(a + "\t" + b + "\t" + c + "\t" + d + "\t" + e.expandtabs(10))
            status = 'open'
        else :
            if 'closed' in s :
                a = Fore.RED + p + Fore.RESET
                b = Fore.RED + s + Fore.RESET
                c = Fore.RED + proto + Fore.RESET
                d = Fore.RED + serv['name'] + Fore.RESET
                e = Fore.RED + res + Fore.RESET
                print(a + "\t" + b + "\t" + c + "\t" + d + "\t" + e.expandtabs(10))
                status = 'closed'
            else :
                a = Fore.YELLOW + p + Fore.RESET
                b = Fore.YELLOW + s + Fore.RESET
                c = Fore.YELLOW + proto + Fore.RESET
                d = Fore.YELLOW + serv['name'] + Fore.RESET
                e = Fore.YELLOW + res + Fore.RESET
                print(a + "\t" + b + "\t" + c + "\t" + d + "\t" + e.expandtabs(10))
                status = 'filtered'
        #print('\033[31m' + f"{p}" + "\t" + Fore.WHITE + Fore.GREEN + f"{s}" +"\t" + Fore.WHITE + f"{proto}" + "\t" + Fore.BLUE + f"{serv['name']}" + "\t" + Fore.YELLOW + f"{res}".expandtabs(30))
    print("\n" + Fore.BLUE + f"{hosts[1]}" + Fore.RED + "      [DONE]")
    return hosts,p,s,proto,serv,res


def parse_dns(s2):
    console.print('\nBRUTEFORCE DNS :', style="bold red")
    bruted_hostname = nested_lookup('hostname', s2)
    bruted_ipv4 = s = socket.gethostbyname(bruted_hostname[1])
    console.print(f"{bruted_ipv4} : {bruted_hostname[1]}")

def parse_os(s4):
    console.print('\nOS RECON : ', style="bold red")
    os_name = nested_lookup('name', s4)
    os_accuracy = nested_lookup('accuracy', s4)
    os_cpe = nested_lookup('cpe', s4)
    os_class = nested_lookup('osfamily', s4)
    console.print(f'{ os_name[0] }')
    console.print(f'{ os_cpe[0] }')
    console.print(f'{ os_accuracy[0] } %', style='bold red')


def main(h,m):
    global console
    console = Console()
    init(autoreset=True)
    if 'LOAD' in m :
        manager.restore()
    elif 'AI' :
        #THREAD TOP SCAN
        t1 = threading.Thread(target=scan_top, args=(h,))
        t1.start()
        while t1.is_alive():
            anime.run1()
        parse_top(s1)
        #THREAD BRUTEFORCE DNS
        t2 = threading.Thread(target=scan_dns, args=(h,))
        t2.start()
        while t2.is_alive():
            anime.run2()
        parse_dns(s2)
        #THREAD OS DETECTION
        t3 = threading.Thread(target=scan_os, args=(h,))
        t3.start()
        while t3.is_alive():
            anime.run2()
        parse_os(s4)

        #scan_dns(h)
        #scan_os(h)
        #manager.create(s1,s2,s4)
    else :
        console.print('Les données n\'ont pas pu être traitées')
    """scan_list(h)
    scan_os(h)
    scan_subnet(h)
    scan_vers(h)"""
if __name__ == '__main__':
    main()
