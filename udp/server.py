import socketserver
from random import randint

ANSWER_WAS_FOUND = False
MIN_BOUND = 1
MAX_BOUND = 100000
goal = randint(MIN_BOUND, MAX_BOUND)


class UDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        global goal
        global ANSWER_WAS_FOUND

        SUCCESS_MESSAGE = "You Won: answer was {}".format(goal)
        GAMEOVER_MESSAGE = "You lost: answer was {}".format(goal)
        GREATER_MESSAGE = "-1"
        LESS_MESSAGE = "0"

        data, client = self.request

        if ANSWER_WAS_FOUND:
            client.sendto(GAMEOVER_MESSAGE.encode(), self.client_address)
            return

        data = data.decode()

        try:
            data = int(data)
        except Exception:
            print("Bad input")
            return

        # print(data)

        if data == goal:
            ANSWER_WAS_FOUND = True
            client.sendto(SUCCESS_MESSAGE.encode(), self.client_address)
            print("Answer found.")
        elif data < goal:
            client.sendto(LESS_MESSAGE.encode(), self.client_address)
        elif data > goal:
            client.sendto(GREATER_MESSAGE.encode(), self.client_address)


if __name__ == "__main__":
    address = ('localhost', 3000)
    server = socketserver.UDPServer(address, UDPHandler)
    print("Server is up and running ...")
    server.serve_forever()
