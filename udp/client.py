from random import randint
from socket import AF_INET, SOCK_DGRAM, socket

server_address = ('localhost', 3000)
GREATER_MESSAGE = "-1"
LESS_MESSAGE = "0"

MIN_BOUND = 1
MAX_BOUND = 100000

client = socket(AF_INET, SOCK_DGRAM)

while True:
    guess = randint(MIN_BOUND, MAX_BOUND)

    client.sendto(str(guess).encode(), server_address)

    data, addr = client.recvfrom(1024)

    data = data.decode()

    if data == GREATER_MESSAGE:
        # MAX_BOUND = guess - 1
        pass
    elif data == LESS_MESSAGE:
        # MIN_BOUND = guess + 1
        pass
    else:
        print(data)
        break
