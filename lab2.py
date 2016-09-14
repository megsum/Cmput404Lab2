import socket

# Allocate a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Listen on port 8000
server.bind(('0.0.0.0', 8000))
server.listen(1)

print "Waiting for connections..."
client, address = server.accept()
print "Connected!"
print address

#client is going to be curl, web browser, etc.
outgoing = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
outgoing.connect(("www.google.ca", 80))
while True:
    part = client.recv(1024)
    print " < " + part
    if (part):
       outgoing.sendall(part)
    part = outgoing.recv(1024)
    print " > " + part
    if (part):
       client.sendall(part)