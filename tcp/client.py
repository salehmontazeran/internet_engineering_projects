from socket import AF_INET, SOCK_STREAM, socket

server_address = ('localhost', 2000)

client = socket(AF_INET, SOCK_STREAM)
client.connect(server_address)

dummy_message = "Just something\n"
client.send(dummy_message.encode())
server_response = client.recv(1024)
client.close()

print("Time is: ", server_response.decode())
