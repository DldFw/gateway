#!/usr/bin/env python
# coding: utf-8

import pyjsonrpc
import json

http_client = pyjsonrpc.HttpClient(
    url = "http://localhost:8090",
    username = "dev",
    password = "a"
)

def account(address):
    params = [1]
    params.append(address)
    data = http_client.call("account", params)
    print data

    params[0] = 2
    data = http_client.call("account", params)
    print data
    
    params[1] = "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"
    data = http_client.call("account", params)
    print data
     
def ledger(ledger_hash):
    params = [1]
    params.append(ledger_hash)
    data = http_client.call("ledger", params)
    

def tx(tx_params):
    params = [1]
    params.append(tx_params)
    data = http_client.call("tx", params)

#params = ["rN7n7otQDd6FczFgLdSqtcsAUxDkw6fzRH", 12, "adadf"]
#print http_client.call("account", params)
#print http_client.call("tx", params)
#print http_client.call("ledger", params)

#params_account_channels = {"account": "rN7n7otQDd6FczFgLdSqtcsAUxDkw6fzRH","destination_account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn","ledger_index": "validated"}

#print http_client.call("account_channels", params_account_channels)

#params_account_currencies = {"account": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh","account_index": 0,"ledger_index": "validated","strict": true}

#print http_client.account_currencies(params_account_currencies)

def main():
    address = "ragYmrzqVbVjA7rpRp2BNCgPqTMzthuA6"
    data = account(address)
    ledger_hash = "69CDBA84285B24077965BC1D8C5107A469C635C3EFEDD496223D698A44FA1AD0"
    data = ledger(ledger_hash)

    tx_params = ["snoPBrXtMeMyMHUVTgbuqAfg1SUTb"]
    tx_params.append("rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh")
    tx_params.append("USD")
    tx_params.append(10000)
    tx_params.append("ragYmrzqVbVjA7rpRp2BNCgPqTMzthuA6")
    tx_params.append("Payment")
    tx_params.append(1000)
    data = tx(tx_params)

if __name__ == '__main__':
    main()
