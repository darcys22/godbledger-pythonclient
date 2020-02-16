### Python client for godbledger

To get started with a python script you will need a copy of the protobuffers.

```
wget https://raw.githubusercontent.com/darcys22/godbledger/master/proto/transaction.proto
```

Install the GRPC pip
```
pip install grpcio-tools
```

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./transaction.proto
```
this will generate 2 py files that can be imported with the following in your script

```
import transaction_pb2
import transaction_pb2_grpc
```




