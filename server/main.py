#!/usr/bin/env python
# coding: utf-8

import pyjsonrpc
import gatewayhandler

http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = ("localhost", 8090),
    RequestHandlerClass = gatewayhandler.RequestHandler
    )

print "Starting HTTP server ..."
print "URL:http://localhost:8090"

def main():
    http_server.serve_forever()

if __name__ == '__main__':
    main()
