"""The Python implementation of the gRPC Godbledger client."""

from __future__ import print_function

import random
import logging

import grpc

import transaction_pb2
import transaction_pb2_grpc


def ledger_get_tb(stub, date):
    tb = stub.GetTB(transaction_pb2.TBRequest(date=date))
    for tbline in tb.lines:
        print("{}: {}".format(tbline.accountname, tbline.amount))
        for tag in tbline.tags:
            print("       {}".format(tag))


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = transaction_pb2_grpc.TransactorStub(channel)
        print("-------------- GetTB --------------")
        ledger_get_tb(stub, "30/06/2019")


if __name__ == '__main__':
    logging.basicConfig()
    run()
