#!/usr/bin/python
import SocketServer  
from SocketServer import StreamRequestHandler as SRH  
from time import ctime  
  
host = '115.29.210.103'  
port = 10119  
addr = (host,port)  
  
class Servers(SRH):  
    def handle(self):  
        print 'got connection from ',self.client_address  
        self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
        while True:  
            data = self.request.recv(1024)  
            if not data:   
                break  
            print data  
            print "RECV from ", self.client_address[0]," at ",self.client_address[1]  
            self.request.send(data)  
print 'server is running....'  
server = SocketServer.ThreadingTCPServer(addr,Servers)  
server.serve_forever()