import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localfqdn = socket.getfqdn()

ip_address = "133.11.164.143" #socket.gethostbyname("")

server_address = (ip_address, 7777)
sock.connect(server_address)
print("Connecting to %s (%s) at %s" % (local_hostname, localfqdn, ip_address))

randomData = ["ls", "pwd","git --version", "cd ../;pwd;ls"] # python --version doesn't seem to work!!  "homebrew --version"]
for ele in randomData:
    print("command is: ", str(ele))
    sock.sendall(ele.encode())
    print("after sendall")
    data = sock.recv(1024)
    print("after recv")
    dat = data.decode("utf-8")
    print ("Data from server: %s" % dat)

sock.close()
