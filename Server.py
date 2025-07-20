import http.server
import socketserver
import socket

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("Local IP  ", socket.gethostbyname(socket.gethostname()))
print("Server at PORT  ", PORT)
httpd.serve_forever()
