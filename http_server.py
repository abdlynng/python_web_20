#coding:utf8
import http.server 
import socketserver 

port = 8000
adresse = ("",port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adresse,handler)

print (f"Serveur démarré: {port}")
httpd.serve_forever()
