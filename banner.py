import socket

def main():
    ip='x.x.x.x'
    port=3306

    s=socket.socket()
    s.connect((ip,port))
    s.send('haha',encode())
    banner=s.recv(1024)
    s.close()
    print("banner is {}".format(banner))

    pass