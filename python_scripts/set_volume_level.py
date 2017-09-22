# Imports
import sys
import telnetlib
# Variables
vol = int(sys.argv[1])
host = sys.argv[2]
port = sys.argv[3]
timeout = 60 # seconds
# Math for volume target
target_volume = (vol*2)+1
# Telnet
tn = telnetlib.Telnet(host,port,timeout)
tn.write("?V\n\r")
output = tn.read_until("\r\n")
current_vol = (int(output[3:]))
print current_vol
if target_volume > current_vol:
    for x in range(current_vol,target_volume,2):
        tn.write("VU\r\n")
elif target_volume < current_vol:
    for x in range(current_vol,target_volume,-2):
	tn.write("VD\r\n")

tn.close()
exit
