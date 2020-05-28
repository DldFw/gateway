#!/usr/bin/env python
# coding: utf-8

import pyjsonrpc
import json

http_client = pyjsonrpc.HttpClient(
    url = "http://localhost:8090",
    username = "dev",
    password = "a"
)
print http_client.call("add", 1, 2)

params_account_channels = {"account": "rN7n7otQDd6FczFgLdSqtcsAUxDkw6fzRH","destination_account": "rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn","ledger_index": "validated"}

#print http_client.call("account_channels", params_account_channels)

params_account_currencies = {"account": "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh","account_index": 0,"ledger_index": "validated","strict": true}

#print http_client.account_currencies(params_account_currencies)


