"""The Python implementation of the gRPC Godbledger client."""

from __future__ import print_function

import random
import logging
import sys

import grpc

import transaction_pb2
import transaction_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = transaction_pb2_grpc.TransactorStub(channel)
        print("-------------- Reconciling Transactions --------------")
        splitIDs = []
        for arg in sys.argv[1:]:
            splitIDs.append(arg)
        response = stub.ReconcileTransactions(transaction_pb2.ReconciliationRequest(splitID=splitIDs))
        print(response)

if __name__ == '__main__':
    logging.basicConfig()
    run()
