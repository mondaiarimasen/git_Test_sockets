import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_hostname = socket.gethostname()

localfqdn = socket.getfqdn()

ip_address = socket.gethostbyname("")

print("This is the ip_address of server: ", ip_address)

print("This is a test with %s (%s), at %s", (local_hostname, localfqdn, ip_address))

server_address = (ip_address, 7777)

print("Attempting to bind to the %s", server_address)
sock.bind(server_address)

sock.listen(2)
file = open("testSocketData.dat", "w")
dat = ""
while True:
    print("Currently waiting for a connection")
    connection, client_address = sock.accept()

    try:
        print("Connection from %s", client_address)
        print("Connection is of type: ", type(connection))
        print("client_address is of type: ", type(client_address))
        # receive the data in small chunks and print it
        while True:
            data =  connection.recv(64)
            dat += data.decode("utf-8") 
            if data:
                # output received data
                print ("Data: %s" % data)
            else:
                # no more data -- quit the loop
                file.write(dat)
                print ("no more data.")
                print ("----------------\n")
                break
    finally:
        # Clean up the connection
        connection.close()
