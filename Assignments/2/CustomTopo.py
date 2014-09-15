# 2014.06.13 13:07:45 PDT
"""
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment 2

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta, Muhammad Shahbaz
"""
from mininet.topo import Topo

class CustomTopo(Topo):
    """Simple Data Center Topology"""


    def __init__(self, linkopts1, linkopts2, linkopts3, fanout = 3, **opts):
        Topo.__init__(self, **opts)
        host_count = 0
        edge_count = 0
        agg_count = 0
        self.fanout = fanout
        c1 = self.addSwitch('c1')

        for a in range(0, fanout):
            agg_count += 1
            switch_a = self.addSwitch("a%s" % agg_count)
            self.addLink(switch_a, c1, **linkopts1)

            for e in range(0, fanout):
                edge_count += 1
                switch_e = self.addSwitch("e%s" % edge_count)
                self.addLink(switch_e, switch_a, **linkopts2)

                for h in range(0, fanout):
                    host_count += 1
                    host = self.addHost("h%s" % host_count, cpu=.5/fanout)
                    self.addLink(host, switch_e, **linkopts3)






linkopts1 = dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
linkopts2 = dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
linkopts3 = dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
fanout = 3
topos = {'custom': lambda : CustomTopo(linkopts1, linkopts1, linkopts1, fanout)}
