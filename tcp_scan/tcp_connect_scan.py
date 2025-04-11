from scapy.all import *

ip='x.x.x.x'#please change as you need
port=80

packet=IP(dst=ip)/TCP(sport=12345,dport=80，flags="S")#(sport=任意)
resp=sr1(packet,time(sport=20))
if str((type(resp))=="<type 'NoneType'>"):
    print("port %s is closed"%(port))
elif(resp.haslayer(TCP)):
    if(resp.getlayer(TCP).flags==0x12):
        send_rst=sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="AR"),timeout=20)
        print("port %s is down"%(port))
    elif(resp.getlayer(TCP).flags==0x14):
        print("port %s is down"%(port))