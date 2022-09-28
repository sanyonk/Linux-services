import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1303
client.connect((host, port))
data = client.recv(1024)
print(data.decode())
client.close()