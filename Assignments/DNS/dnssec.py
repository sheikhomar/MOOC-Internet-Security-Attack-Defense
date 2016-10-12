#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.term import makeTerms
from mininet.clean import Cleanup

import os
import signal

class DDoSTopo(Topo):
    def build(self):
        #Single switch
        switch = self.addSwitch('s1')
   	
	#Add attacker, dns resolver and victim host nodes
        attacker = self.addHost('A')
        dnsresolver = self.addHost('B')
        victim = self.addHost('C')
        capture = self.addHost('D')

        #Add links between each of the hosts and the switch
        self.addLink(attacker,switch)
        self.addLink(dnsresolver,switch)
        self.addLink(victim,switch)
	self.addLink(capture,switch)

def run_exercise():
    #Create and start a new network with our custom topology
    topo = DDoSTopo()
    net = Mininet(topo=topo)
    net.start()

    #Configure switch so that packets reach the right port (to prevent l2 learning from affecting the exercise)
    net["s1"].dpctl("del-flows")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=1,nw_dst=10.0.0.1,actions=output:1,mod_vlan_vid:11,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=1,nw_dst=10.0.0.2,actions=output:2,mod_vlan_vid:11,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=1,nw_dst=10.0.0.3,actions=output:3,mod_vlan_vid:11,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=2,nw_dst=10.0.0.1,actions=output:1,mod_vlan_vid:12,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=2,nw_dst=10.0.0.2,actions=output:2,mod_vlan_vid:12,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=2,nw_dst=10.0.0.3,actions=output:3,mod_vlan_vid:12,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=3,nw_dst=10.0.0.1,actions=output:1,mod_vlan_vid:13,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=3,nw_dst=10.0.0.2,actions=output:2,mod_vlan_vid:13,output:4")
    net["s1"].dpctl("add-flow", "dl_type=0x0800,in_port=3,nw_dst=10.0.0.3,actions=output:3,mod_vlan_vid:13,output:4")

    #Verify connectivity
    net.pingAll()

    processes = []

    #Start BIND DNS-server
    processes.append(net["B"].popen('named', '-g', '-c', '/home/vagrant/assignments/DNS/config/named.conf'))

    #Open terminals
    processes.append(makeTerms([net["A"]], title="Attacker terminal")[0])
    processes.append(makeTerms([net["D"]], title="Capture terminal")[0])
    raw_input("Press Enter to exit....")
    for process in processes:
        process.kill()
    Cleanup.cleanup()

if __name__ == '__main__':
    run_exercise()

