"""The Python implementation of the gRPC Godbledger client."""

from __future__ import print_function

import random
import logging

import grpc

import transaction_pb2
import transaction_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = transaction_pb2_grpc.TransactorStub(channel)
        print("-------------- Sending Transaction --------------")
        response = stub.AddTransaction(transaction_pb2.TransactionRequest(
            date="2019-06-30",
            description="Sales",
            lines=[
                transaction_pb2.LineItem(
                    accountname="Income",
                    description="Some Specifics",
                    amount=-1000),
                transaction_pb2.LineItem(
                    accountname="Cash",
                    description="Some Specifics",
                    amount=1000)
                ],
            signature="Not Implemented"
            ))


if __name__ == '__main__':
    logging.basicConfig()
    run()
