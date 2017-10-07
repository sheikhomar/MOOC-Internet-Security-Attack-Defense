from __future__ import print_function
from scapy.all import *

answer = sr1(IP(dst='10.0.0.2', src='10.0.0.3')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='smooth-computer-hunter.security.utwente.nl', qtype='A')), verbose=1)
