import sys
import getpass
import telnetlib

tnCommand = sys.argv[1]
host = sys.argv[2]
port = sys.argv[3]


tn=telnetlib.Telnet(host,port)
tn.write(tnCommand + "\n\r")
tn.close()

exit
