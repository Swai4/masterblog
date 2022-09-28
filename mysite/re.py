import socket
s = socket.socket()
s.connect(('192.168.43.27',8080))
ans = s.recv(1024)
print(ans)
