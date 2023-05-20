import socket

target_host = "192.46.223.87"
target_port = 9998

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to client
client.connect((target_host,target_port))

#send some data to target
client.send(b"H@<k th3 P1@net")

#client.send(b"GET / HTTP/1.1\r\nHost: jordanrobbinsresume.com\r\n\r\n")

#rec data
response = client.recv(4096)

print(response.decode())
client.close()