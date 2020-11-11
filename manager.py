import pickle
import os
import scanner
import threading
import server
"""
def check():
    if os.path.isfile('*.pickle'):
        os.system("mv *.pickle /bd/")

    else:

"""

def create(s1,s2,s4):
    global scan_top
    global scan_dns
    global scan_list
    global scan_os
    global scan_subnet
    global scan_version

    scan_top = open("bd/scan_top.pickle", "wb")
    pickle.dump(s1, scan_top)

    scan_dns = open("bd/scan_dns.pickle", "wb")
    pickle.dump(s2, scan_dns)

    scan_os = open("bd/scan_os.pickle", "wb")
    pickle.dump(s4, scan_os)
    return scan_top, scan_dns,scan_os
    """
    scan_list = open("bd/scan_list.pickle", "wb")
    pickle.dump(s3, scan_list)
    scan_subnet = open("bd/scan_subnet.pickle", "wb")
    pickle.dump(s5, scan_subnet)

    scan_version = open("bd/scan_version.pickle", "wb")
    pickle.dump(s6, scan_version)
"""

def restore():
    scan_top = open("bd/scan_top.pickle","rb")
    s1 = pickle.load(scan_top)
    scan_dns = open("bd/scan_dns.pickle","rb")
    s2 = pickle.load(scan_dns)
    scan_os = open("bd/scan_os.pickle","rb")
    s4 = pickle.load(scan_os)
    scanner.parse_top(s1)
    scanner.parse_dns(s2)
    scanner.parse_os(s4)
    t1 = threading.Thread(target=server.run())
    t1.start()
    """s2 = pickle.load(scan_dns)
    s3 = pickle.load(scan_list)
    s4 = pickle.load(scan_os)
    s5 = pickle.load(scan_subnet)
    s6 = pickle.load(scan_version)"""
    return s1,s2,s4

def explorer():
    pass
