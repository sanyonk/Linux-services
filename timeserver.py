import socket
import sys
import datetime

host = socket.gethostname()
port = 1303
dt = datetime.datetime.now()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen(5)

while True:
	try:
		user, addr = server.accept()
		dt = datetime.datetime.now()
		msg = dt.strftime("%d.%m.%Y %H:%M")
		user.send(msg.encode())
		
	except KeyboardInterrupt:
		
		sys.exit(1)