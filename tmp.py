import nmap3
import anime
from threading import Thread
import time
import progressbar

def scan():
    bar = progressbar.ProgressBar()
    nm = nmap3.Nmap()
    for i in bar(range(100)):
        r = nm.scan_top_ports('scanme.nmap.org')


if __name__ == '__main__':
    scan()
