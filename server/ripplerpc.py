#!/usr/bin/env python
# coding: utf-8

import pyjsonrpc
import json
import logging

logging.basicConfig(filename = "ripplerpc.log", level = logging.INFO)

ripple_client = pyjsonrpc.HttpClient(
    url = "http://localhost:5005",
    username = "dev",
    password = "a"
)

class rippleRpc:
    sys_addr = "rHb9CJAWyB4rj91VRWn96DkukG4bwdtyTh"
    sys_key = "snoPBrXtMeMyMHUVTgbuqAfg1SUTb"
    def __init__(self):
        logging.info("init ripple rpc")

    def channels(self, destination):
        params_channels = {}
        params_channels["account"] = self.sys_addr
        params_channels["destination_account"] = destination
        params_channels["ledger_index"] = "validated"
        result = ripple_client.call("account_channels", params_channels)
        logging.info(json.dumps(result, indent = 4))
        return result

    def info(self, destination):
        params_currencies = {}
        params_currencies["account"] = destination
        params_currencies["account_index"] = 0
        params_currencies["ledger_index"] = "validated"
        params_currencies["strict"] = True
        result = ripple_client.call("account_currencies", params_currencies)
        logging.info(json.dumps(result, indent = 4))
        
        params_info = {}
        params_info["account"] = destination
        params_info["queue"] = True
        params_info["ledger_index"] = "current"
        params_info["strict"] = True
        result = ripple_client.call("account_info", params_info)
        logging.info(json.dumps(result, indent = 4))
        
        params_lines = {}
        params_lines["account"] = destination
        result = ripple_client.call("account_lines", params_lines)
        logging.info(json.dumps(result, indent = 4))

        params_objects = {}
        params_objects["account"] = destination
        params_objects["ledger_index"] = "validated"
        params_objects["type"] = "state"
        params_objects["deletion_blockers_only"] = False
        params_objects["limit"] = 10 
        result = ripple_client.call("account_objects", params_objects)
        logging.info(json.dumps(result, indent = 4))

        params_offers = {}
        params_offers["account"] = destination
        result = ripple_client.call("account_offers", params_offers)
        logging.info(json.dumps(result, indent = 4))

        params_tx = {}
        params_tx["account"] = destination
        params_tx["binary"] = False
        params_tx["forward"] = False
        params_tx["ledger_index_max"] = -1
        params_tx["ledger_index_min"] = -1
        params_tx["limit"] = 2  
        result = ripple_client.call("account_tx", params_offers)
        logging.info(json.dumps(result, indent = 4))
        
        hotwallet = []
        hotwallet.append(self.sys_addr)
        hotwallet.append(destination)
        params_gateway_balances = {}
        params_gateway_balances["account"] = destination;
        params_gateway_balances["hotwallet"] = hotwallet;
        params_gateway_balances["ledger_index"] = "validated";
        params_gateway_balances["strict"] = True;
        result = ripple_client.call("gateway_balances", params_gateway_balances)
        logging.info(json.dumps(result, indent = 4))

        params_noripple_check = {}
        params_noripple_check["account"] = destination
        params_noripple_check["ledger_index"] = "current"
        params_noripple_check["limit"] = 2
        params_noripple_check["role"] = "gateway"
        params_noripple_check["transactions"] = True
        logging.info(json.dumps(result, indent = 4))

        return result

    def ledger(self, ledger_hash):
        params_ledger = {}
        params_ledger["ledger_index"] = "validated"
        params_ledger["accounts"] = False
        params_ledger["full"] = False
        params_ledger["transactions"] = False
        params_ledger["expand"] = False
        params_ledger["owner_funds"] = False
        result = ripple_client.call("ledger", params_ledger)
        logging.info(json.dumps(result, indent = 4))

        params_current = {}
        result = ripple_client.call("ledger_current", params_current)
        logging.info(json.dumps(result, indent = 4))

        params_data = {}
        params_data["binary"] = True
        params_data["ledger_hash"] = ledger_hash
        params_data["limit"] = 5
        result = ripple_client.call("ledger_data", params_current)
        logging.info(json.dumps(result, indent = 4))

        params_entry = {}
        params_entry["account_root"] = self.sys_addr
        params_entry["ledger_index"] = "validated"
        params_entry["type"] = "account_root" 
        result = ripple_client.call("ledger_entry", params_entry)
        logging.info(json.dumps(result, indent = 4))

    def transfer(self, params):
        params_sign = {}
        params_sign["secret"] = params[0]
        tx_json = {}
        tx_json["Account"] = params[1]
        amount = {}
        amount["currency"] = params[2]
        amount["issuer"] = params[1]
        amount["value"] = params[3]
        tx_json["Amount"] = amount
        tx_json["Destination"] = params[4]
        tx_json["TransactionType"] = params[5]
        params_sign["tx_json"] = tx_json
        params_sign["fee_mult_max"] = params[6]
        result = ripple_client.call("sign", params_sign)
        logging.info(json.dumps(result, indent = 4))
        tx_blob = result["tx_blob"]
        params_submit = {}
        params_submit["tx_blob"] = tx_blob
        result = ripple_client.call("submit", params_submit)
        logging.info(json.dumps(result, indent = 4))

        return result

