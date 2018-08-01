import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localfqdn = socket.getfqdn()

ip_address = "133.11.164.138" #socket.gethostbyname("")

server_address = (ip_address, 7777)
sock.connect(server_address)
print("Connecting to %s (%s) at %s" % (local_hostname, localfqdn, ip_address))

randomData = [243,45242,32,43,5,2,"SDF","123W","313"]
for ele in randomData:
    print("data is: ", str(ele))
    new_data = str("rand1: %s\n" % ele).encode("utf-8")
    sock.sendall(new_data)

sock.close()
