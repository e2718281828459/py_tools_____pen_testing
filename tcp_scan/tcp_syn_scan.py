from scapy.all import *


ip='x.x.x.x'
port=80

packet=IP(dst=ip)/TCP(sport=12345,dport=80，flags="S")#(sport=anything allowed)
resp=sr1(packet,timeout=1.0,verbose=0)
if str((type(resp))=="<type 'NoneType'>"):
    print("port %s is closed"%(port))
elif(resp.haslayer(TCP)):
    if(resp.getlayer(TCP).flags==0x12):
        send_rst=sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="R"),timeout=20)#AR turns to R
        print("port %s is down"%(port))
    elif(resp.getlayer(TCP).flags==0x14):
        print("port %s is down"%(port))
        