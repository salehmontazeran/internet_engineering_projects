import logging
from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from os import curdir, path, sep

logging.basicConfig(
    level=logging.INFO,
    filename="webserver_log.txt",
    format='%(asctime)s  -->  %(message)s'
)

SERVER_ADDRESS = ('localhost', 8080)


class HTTPHandler(BaseHTTPRequestHandler):

    def log_user(self, username, password):
        logging.info("Username: %s    Password: %s" % (username, password))

    def detect_mimetype(self):
        mime = [(".html", "text/html"),
                (".jpg", "image/jpg"),
                (".gif", "image/gif"),
                (".js", "application/javascript"),
                (".css", "text/css")
                ]
        for pair in mime:
            if self.path.endswith(pair[0]):
                return True, pair[1]
        return False, ""

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        ok, mimetype = self.detect_mimetype()
        if ok:
            try:
                file_path = curdir + sep + self.path
                if path.isfile(file_path):
                    self.send_response(200)
                    self.send_header('Content-Type', mimetype)
                    self.end_headers()
                    with open(curdir + sep + self.path, 'rb') as file:
                        self.wfile.write(file.read())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b"File not found.")
            except Exception as e:
                self.send_error(404, e)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Mimetype was not recognized.")

    def do_POST(self):
        if self.path == "/send":
            form = FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': 'POST',
                    'CONTENT_TYPE': self.headers['Content-Type']
                }
            )

            if "username" in form and "password" in form:
                username = form["username"].value
                password = form["password"].value
                self.log_user(username, password)
            else:
                username = ""
                password = ""

            if (username == "saleh" and password == "123"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Hello World!")
            else:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Forbidden")


if __name__ == "__main__":
    try:
        server = ThreadingHTTPServer(SERVER_ADDRESS, HTTPHandler)
        print("HTTP server is up and running ...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server ...")
        server.socket.close()
