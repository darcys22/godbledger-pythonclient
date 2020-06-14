# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='transaction',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11transaction.proto\x12\x0btransaction\"V\n\x08LineItem\x12\x13\n\x0b\x61\x63\x63ountname\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x63urrency\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\"p\n\x12TransactionRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12$\n\x05lines\x18\x03 \x03(\x0b\x32\x15.transaction.LineItem\x12\x11\n\tsignature\x18\x04 \x01(\t\"6\n\rDeleteRequest\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\t\"&\n\x13TransactionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"=\n\nTagRequest\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\t\"C\n\x10\x44\x65leteTagRequest\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\t\"H\n\x0f\x43urrencyRequest\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x02 \x01(\x03\x12\x11\n\tsignature\x18\x03 \x01(\t\"<\n\x15\x44\x65leteCurrencyRequest\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\t\"r\n\x06TBLine\x12\x13\n\x0b\x61\x63\x63ountname\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x10\n\x08\x63urrency\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x05 \x01(\x03\x12\x11\n\tamountStr\x18\x06 \x01(\t\"\x19\n\tTBRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"0\n\nTBResponse\x12\"\n\x05lines\x18\x01 \x03(\x0b\x32\x13.transaction.TBLine\"!\n\x0eVersionRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x0fVersionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x82\x05\n\nTransactor\x12J\n\x0bNodeVersion\x12\x1b.transaction.VersionRequest\x1a\x1c.transaction.VersionResponse\"\x00\x12U\n\x0e\x41\x64\x64Transaction\x12\x1f.transaction.TransactionRequest\x1a .transaction.TransactionResponse\"\x00\x12S\n\x11\x44\x65leteTransaction\x12\x1a.transaction.DeleteRequest\x1a .transaction.TransactionResponse\"\x00\x12\x45\n\x06\x41\x64\x64Tag\x12\x17.transaction.TagRequest\x1a .transaction.TransactionResponse\"\x00\x12N\n\tDeleteTag\x12\x1d.transaction.DeleteTagRequest\x1a .transaction.TransactionResponse\"\x00\x12O\n\x0b\x41\x64\x64\x43urrency\x12\x1c.transaction.CurrencyRequest\x1a .transaction.TransactionResponse\"\x00\x12X\n\x0e\x44\x65leteCurrency\x12\".transaction.DeleteCurrencyRequest\x1a .transaction.TransactionResponse\"\x00\x12:\n\x05GetTB\x12\x16.transaction.TBRequest\x1a\x17.transaction.TBResponse\"\x00\x62\x06proto3'
)




_LINEITEM = _descriptor.Descriptor(
  name='LineItem',
  full_name='transaction.LineItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountname', full_name='transaction.LineItem.accountname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='transaction.LineItem.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='transaction.LineItem.currency', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.LineItem.amount', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=120,
)


_TRANSACTIONREQUEST = _descriptor.Descriptor(
  name='TransactionRequest',
  full_name='transaction.TransactionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='transaction.TransactionRequest.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='transaction.TransactionRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lines', full_name='transaction.TransactionRequest.lines', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='transaction.TransactionRequest.signature', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=234,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='transaction.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='transaction.DeleteRequest.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='transaction.DeleteRequest.signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=290,
)


_TRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='TransactionResponse',
  full_name='transaction.TransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='transaction.TransactionResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=330,
)


_TAGREQUEST = _descriptor.Descriptor(
  name='TagRequest',
  full_name='transaction.TagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='transaction.TagRequest.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='transaction.TagRequest.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='transaction.TagRequest.signature', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=332,
  serialized_end=393,
)


_DELETETAGREQUEST = _descriptor.Descriptor(
  name='DeleteTagRequest',
  full_name='transaction.DeleteTagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='transaction.DeleteTagRequest.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='transaction.DeleteTagRequest.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='transaction.DeleteTagRequest.signature', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=462,
)


_CURRENCYREQUEST = _descriptor.Descriptor(
  name='CurrencyRequest',
  full_name='transaction.CurrencyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='transaction.CurrencyRequest.currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decimals', full_name='transaction.CurrencyRequest.decimals', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='transaction.CurrencyRequest.signature', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=536,
)


_DELETECURRENCYREQUEST = _descriptor.Descriptor(
  name='DeleteCurrencyRequest',
  full_name='transaction.DeleteCurrencyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='transaction.DeleteCurrencyRequest.currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='transaction.DeleteCurrencyRequest.signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=598,
)


_TBLINE = _descriptor.Descriptor(
  name='TBLine',
  full_name='transaction.TBLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountname', full_name='transaction.TBLine.accountname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='transaction.TBLine.tags', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.TBLine.amount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='transaction.TBLine.currency', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decimals', full_name='transaction.TBLine.decimals', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amountStr', full_name='transaction.TBLine.amountStr', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=600,
  serialized_end=714,
)


_TBREQUEST = _descriptor.Descriptor(
  name='TBRequest',
  full_name='transaction.TBRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='transaction.TBRequest.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=741,
)


_TBRESPONSE = _descriptor.Descriptor(
  name='TBResponse',
  full_name='transaction.TBResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lines', full_name='transaction.TBResponse.lines', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=791,
)


_VERSIONREQUEST = _descriptor.Descriptor(
  name='VersionRequest',
  full_name='transaction.VersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='transaction.VersionRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=793,
  serialized_end=826,
)


_VERSIONRESPONSE = _descriptor.Descriptor(
  name='VersionResponse',
  full_name='transaction.VersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='transaction.VersionResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=862,
)

_TRANSACTIONREQUEST.fields_by_name['lines'].message_type = _LINEITEM
_TBRESPONSE.fields_by_name['lines'].message_type = _TBLINE
DESCRIPTOR.message_types_by_name['LineItem'] = _LINEITEM
DESCRIPTOR.message_types_by_name['TransactionRequest'] = _TRANSACTIONREQUEST
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['TransactionResponse'] = _TRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['TagRequest'] = _TAGREQUEST
DESCRIPTOR.message_types_by_name['DeleteTagRequest'] = _DELETETAGREQUEST
DESCRIPTOR.message_types_by_name['CurrencyRequest'] = _CURRENCYREQUEST
DESCRIPTOR.message_types_by_name['DeleteCurrencyRequest'] = _DELETECURRENCYREQUEST
DESCRIPTOR.message_types_by_name['TBLine'] = _TBLINE
DESCRIPTOR.message_types_by_name['TBRequest'] = _TBREQUEST
DESCRIPTOR.message_types_by_name['TBResponse'] = _TBRESPONSE
DESCRIPTOR.message_types_by_name['VersionRequest'] = _VERSIONREQUEST
DESCRIPTOR.message_types_by_name['VersionResponse'] = _VERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LineItem = _reflection.GeneratedProtocolMessageType('LineItem', (_message.Message,), {
  'DESCRIPTOR' : _LINEITEM,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.LineItem)
  })
_sym_db.RegisterMessage(LineItem)

TransactionRequest = _reflection.GeneratedProtocolMessageType('TransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.TransactionRequest)
  })
_sym_db.RegisterMessage(TransactionRequest)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

TransactionResponse = _reflection.GeneratedProtocolMessageType('TransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONRESPONSE,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.TransactionResponse)
  })
_sym_db.RegisterMessage(TransactionResponse)

TagRequest = _reflection.GeneratedProtocolMessageType('TagRequest', (_message.Message,), {
  'DESCRIPTOR' : _TAGREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.TagRequest)
  })
_sym_db.RegisterMessage(TagRequest)

DeleteTagRequest = _reflection.GeneratedProtocolMessageType('DeleteTagRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETAGREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.DeleteTagRequest)
  })
_sym_db.RegisterMessage(DeleteTagRequest)

CurrencyRequest = _reflection.GeneratedProtocolMessageType('CurrencyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CURRENCYREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.CurrencyRequest)
  })
_sym_db.RegisterMessage(CurrencyRequest)

DeleteCurrencyRequest = _reflection.GeneratedProtocolMessageType('DeleteCurrencyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECURRENCYREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.DeleteCurrencyRequest)
  })
_sym_db.RegisterMessage(DeleteCurrencyRequest)

TBLine = _reflection.GeneratedProtocolMessageType('TBLine', (_message.Message,), {
  'DESCRIPTOR' : _TBLINE,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.TBLine)
  })
_sym_db.RegisterMessage(TBLine)

TBRequest = _reflection.GeneratedProtocolMessageType('TBRequest', (_message.Message,), {
  'DESCRIPTOR' : _TBREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.TBRequest)
  })
_sym_db.RegisterMessage(TBRequest)

TBResponse = _reflection.GeneratedProtocolMessageType('TBResponse', (_message.Message,), {
  'DESCRIPTOR' : _TBRESPONSE,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.TBResponse)
  })
_sym_db.RegisterMessage(TBResponse)

VersionRequest = _reflection.GeneratedProtocolMessageType('VersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONREQUEST,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.VersionRequest)
  })
_sym_db.RegisterMessage(VersionRequest)

VersionResponse = _reflection.GeneratedProtocolMessageType('VersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONRESPONSE,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.VersionResponse)
  })
_sym_db.RegisterMessage(VersionResponse)



_TRANSACTOR = _descriptor.ServiceDescriptor(
  name='Transactor',
  full_name='transaction.Transactor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=865,
  serialized_end=1507,
  methods=[
  _descriptor.MethodDescriptor(
    name='NodeVersion',
    full_name='transaction.Transactor.NodeVersion',
    index=0,
    containing_service=None,
    input_type=_VERSIONREQUEST,
    output_type=_VERSIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddTransaction',
    full_name='transaction.Transactor.AddTransaction',
    index=1,
    containing_service=None,
    input_type=_TRANSACTIONREQUEST,
    output_type=_TRANSACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTransaction',
    full_name='transaction.Transactor.DeleteTransaction',
    index=2,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_TRANSACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddTag',
    full_name='transaction.Transactor.AddTag',
    index=3,
    containing_service=None,
    input_type=_TAGREQUEST,
    output_type=_TRANSACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTag',
    full_name='transaction.Transactor.DeleteTag',
    index=4,
    containing_service=None,
    input_type=_DELETETAGREQUEST,
    output_type=_TRANSACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddCurrency',
    full_name='transaction.Transactor.AddCurrency',
    index=5,
    containing_service=None,
    input_type=_CURRENCYREQUEST,
    output_type=_TRANSACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteCurrency',
    full_name='transaction.Transactor.DeleteCurrency',
    index=6,
    containing_service=None,
    input_type=_DELETECURRENCYREQUEST,
    output_type=_TRANSACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTB',
    full_name='transaction.Transactor.GetTB',
    index=7,
    containing_service=None,
    input_type=_TBREQUEST,
    output_type=_TBRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSACTOR)

DESCRIPTOR.services_by_name['Transactor'] = _TRANSACTOR

# @@protoc_insertion_point(module_scope)
