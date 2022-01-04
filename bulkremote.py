"""The Python implementation of the gRPC Godbledger client. Sends bulk transactions using generatedExpenses.json and generatedIncome.json to a remote server"""

from __future__ import print_function

import random
import logging

import grpc
import json

import transaction_pb2
import transaction_pb2_grpc

from tqdm import tqdm


def run():
    with grpc.insecure_channel('play.godbledger.com:50051') as channel:
        stub = transaction_pb2_grpc.TransactorStub(channel)
        with open('generatedIncome.json') as f:
            incometransactions = json.load(f)
            print("-------------- Sending Income Transactions --------------")
            for transaction in tqdm(incometransactions):
                response = stub.AddTransaction(transaction_pb2.TransactionRequest(
                    date= transaction["date"][0:10],
                    description= transaction["description"],
                    lines=[
                        transaction_pb2.LineItem(
                            accountname= transaction["account"],
                            description= transaction["description"],
                            amount=-transaction["balance"]),
                        transaction_pb2.LineItem(
                            accountname="Cash",
                            description= transaction["description"],
                            amount=transaction["balance"])
                        ]
                    ))
                # print(response)
                # quit()
        with open('generatedExpenses.json') as f:
            expensetransactions = json.load(f)
            print("-------------- Sending Expense Transactions --------------")
            for transaction in tqdm(expensetransactions):
                response = stub.AddTransaction(transaction_pb2.TransactionRequest(
                    date= transaction["date"][0:10],
                    description= transaction["description"],
                    lines=[
                        transaction_pb2.LineItem(
                            accountname= transaction["account"],
                            description= transaction["description"],
                            amount=transaction["balance"]),
                        transaction_pb2.LineItem(
                            accountname="Cash",
                            description= transaction["description"],
                            amount=-transaction["balance"])
                        ]
                    ))
                # print(response)
                # quit()


if __name__ == '__main__':
    logging.basicConfig()
    run()
