import socket

# Allocate a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to google.ca
server.bind(('0.0.0.0', 8000))
server.listen(1)

print "Waiting for connections..."
client, address = server.accept()
print "Connected!"
print address
