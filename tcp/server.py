import socketserver
from datetime import datetime

welcome_message = "NTP server is up & running ..."
PORT_ADDRESS = 2000


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Connected: ", self.client_address)
        time = datetime.now()

        self.request.recv(1024)

        self.request.send(str(time).encode())


if __name__ == "__main__":
    address = ('localhost', PORT_ADDRESS)
    server = socketserver.TCPServer(address, TCPHandler)
    print(welcome_message)
    server.serve_forever()
