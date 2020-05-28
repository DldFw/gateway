#!/usr/bin/env python
# coding: utf-8

import ripplerpc
import pyjsonrpc
import json
import logging

client = ripplerpc.rippleRpc()

class RequestHandler(pyjsonrpc.HttpRequestHandler):

    def printRpc(self, method, params):
        log_rpc = {};
        log_rpc["method"] = method
        log_rpc["params"] = params
        logging.warn(json.dumps(log_rpc, indent = 4))

    @pyjsonrpc.rpcmethod
    def account(self, params):
        handle_type = params[0]
        self.printRpc("account", params)
        destination = params[1]
        ret = {"code":0}
        if handle_type == 1:
            ret["result"] = client.channels(destination)
        elif handle_type == 2:
            ret["result"] = client.info(destination)

        logging.info(json.dumps(ret, indent = 4))
        return ret

    @pyjsonrpc.rpcmethod
    def ledger(self, params):
        handle_type = params[0]
        self.printRpc("lodger", params)
        ledger_hash = params[1]

        ret = {"code":0}
        if handle_type == 1:
            ret["result"] = client.ledger(ledger_hash)

        logging.info(json.dumps(ret, indent = 4))
        return ret
    
    @pyjsonrpc.rpcmethod
    def tx(self, params):
        handle_type = params[0]
        self.printRpc("tx", params)
        ret = {"code":0}
        ret["result"] = handle_type
        tx_params = params[1]
        if handle_type == 1:
            ret["result"] = client.transfer(tx_params)

        logging.info(json.dumps(ret, indent = 4))
        return ret
