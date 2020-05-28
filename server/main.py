#!/usr/bin/env python
# coding: utf-8

import pyjsonrpc

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        print "rpc method add"
        return a + b

http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = ("localhost", 8090),
    RequestHandlerClass = RequestHandler
    )
print "Starting HTTP server ..."
print "URL:http://localhost:8090"

http_server.serve_forever()

