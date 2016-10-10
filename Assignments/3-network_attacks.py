#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.term import makeTerms
from mininet.node import Node
import random
import re
from shutil import copyfile

import signal 
import sys
import threading
import os

def signal_handler(signal, frame):
    print("got CTRL+C")

signal.signal(signal.SIGINT, signal_handler)

class ExerciseState():
    def __init__(self, net, pid):
        self.bind_pid = pid;
        self.net = net;

class SSHTopo(Topo):
    def build(self):
        #Single switch
        switch = self.addSwitch('s1')
   	
	#Add attacker, dns resolver and victim host nodes
        dns         = self.addHost('DNS', ip='10.0.3.1/24')
        attacker    = self.addHost('A', ip='10.0.3.2/24')
        target1     = self.addHost('T1', ip='10.0.3.11/24')
        target2     = self.addHost('T2', ip='10.0.3.22/24')
        target3     = self.addHost('T3', ip='10.0.3.33/24')
        target4     = self.addHost('T4', ip='10.0.3.44/24')
        target5     = self.addHost('T5', ip='10.0.3.55/24')

        #Add links between each of the hosts and the switch
        self.addLink(dns,switch)
        self.addLink(attacker,switch)
        self.addLink(target1,switch)
        self.addLink(target2,switch)
        self.addLink(target3,switch)
        self.addLink(target4,switch)
        self.addLink(target5,switch)
	


def run_exercise():
    # first backup /etc/resolv.conf, we'll put it back in cleanup()
    copyfile("/etc/resolv.conf", "/tmp/resolv.conf.bak")
    #Create and start a new network with our custom topology
    topo = SSHTopo()
    net = Mininet(topo=topo)
    net.start()

    #Verify connectivity
    #net.pingAll()

    # These commands affect the host VM itself AND all hosts spawned 
    # by mininet. We only need to do it once, on any host in our topo.
    net['DNS'].cmd('echo "nameserver 10.0.3.1" > /etc/resolv.conf')
    net['DNS'].cmd('echo "search mooc" >> /etc/resolv.conf')

    # configure resolv.conf on all hosts:
    for i, host in enumerate(net.hosts):
        host.cmd('ip addr add fc00::3:%i/64 dev %s-eth0' % (i, host.name))
        if re.match('T\d', host.name) is not None:
            host.cmd('/usr/sbin/sshd -p %i -6' % (2230 + i*2))
            for randomport in random.sample(range(1,65535), 20-i):
                #print "listening on %i" %randomport
                host.cmd('/bin/netcat', '-k -l -p %i &' % randomport)

    #Start BIND DNS-server
    bind_pid = net["DNS"].popen('named', '-g', '-c', '/home/vagrant/assignments/3-network_attacks/named.conf').pid

    #makeTerms([net["B"]], title="DNS")	

    #Open terminals
    makeTerms([net["A"]], title="Attacker terminal")

    state = ExerciseState(net, bind_pid)
    return state
     
def cleanup(state):
    copyfile("/tmp/resolv.conf.bak", "/etc/resolv.conf")
    os.kill(state.bind_pid, signal.SIGTERM)
    os.system('sudo mn -c')

if __name__ == '__main__':
    state = run_exercise()

    print("Exercise started, press CTRL+C to stop and clean up")
    signal.pause()
    cleanup(state);
