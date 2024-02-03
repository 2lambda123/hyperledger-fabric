# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ab.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ab.proto',
  package='atomicbroadcast',
  syntax='proto3',
  serialized_pb=_b('\n\x08\x61\x62.proto\x12\x0f\x61tomicbroadcast\"<\n\x11\x42roadcastResponse\x12\'\n\x06Status\x18\x01 \x01(\x0e\x32\x17.atomicbroadcast.Status\" \n\x10\x42roadcastMessage\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\x0c\"\x9f\x01\n\x08SeekInfo\x12\x32\n\x05Start\x18\x01 \x01(\x0e\x32#.atomicbroadcast.SeekInfo.StartType\x12\x17\n\x0fSpecifiedNumber\x18\x02 \x01(\x04\x12\x12\n\nWindowSize\x18\x03 \x01(\x04\"2\n\tStartType\x12\n\n\x06NEWEST\x10\x00\x12\n\n\x06OLDEST\x10\x01\x12\r\n\tSPECIFIED\x10\x02\"!\n\x0f\x41\x63knowledgement\x12\x0e\n\x06Number\x18\x01 \x01(\x04\"\x7f\n\rDeliverUpdate\x12;\n\x0f\x41\x63knowledgement\x18\x01 \x01(\x0b\x32 .atomicbroadcast.AcknowledgementH\x00\x12)\n\x04Seek\x18\x02 \x01(\x0b\x32\x19.atomicbroadcast.SeekInfoH\x00\x42\x06\n\x04Type\"m\n\x05\x42lock\x12\x0e\n\x06Number\x18\x02 \x01(\x04\x12\x10\n\x08PrevHash\x18\x03 \x01(\x0c\x12\r\n\x05Proof\x18\x04 \x01(\x0c\x12\x33\n\x08Messages\x18\x05 \x03(\x0b\x32!.atomicbroadcast.BroadcastMessage\"l\n\x0f\x44\x65liverResponse\x12(\n\x05\x45rror\x18\x01 \x01(\x0e\x32\x17.atomicbroadcast.StatusH\x00\x12\'\n\x05\x42lock\x18\x02 \x01(\x0b\x32\x16.atomicbroadcast.BlockH\x00\x42\x06\n\x04Type*a\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x10\n\x0b\x42\x41\x44_REQUEST\x10\x90\x03\x12\x0e\n\tFORBIDDEN\x10\x93\x03\x12\x0e\n\tNOT_FOUND\x10\x94\x03\x12\x18\n\x13SERVICE_UNAVAILABLE\x10\xf7\x03\x32\xbe\x01\n\x0f\x41tomicBroadcast\x12X\n\tBroadcast\x12!.atomicbroadcast.BroadcastMessage\x1a\".atomicbroadcast.BroadcastResponse\"\x00(\x01\x30\x01\x12Q\n\x07\x44\x65liver\x12\x1e.atomicbroadcast.DeliverUpdate\x1a .atomicbroadcast.DeliverResponse\"\x00(\x01\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='atomicbroadcast.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=1, number=400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORBIDDEN', index=2, number=403,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=3, number=404,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_UNAVAILABLE', index=4, number=503,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=672,
  serialized_end=769,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
SUCCESS = 0
BAD_REQUEST = 400
FORBIDDEN = 403
NOT_FOUND = 404
SERVICE_UNAVAILABLE = 503


_SEEKINFO_STARTTYPE = _descriptor.EnumDescriptor(
  name='StartType',
  full_name='atomicbroadcast.SeekInfo.StartType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEWEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OLDEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIFIED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=235,
  serialized_end=285,
)
_sym_db.RegisterEnumDescriptor(_SEEKINFO_STARTTYPE)


_BROADCASTRESPONSE = _descriptor.Descriptor(
  name='BroadcastResponse',
  full_name='atomicbroadcast.BroadcastResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Status', full_name='atomicbroadcast.BroadcastResponse.Status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=89,
)


_BROADCASTMESSAGE = _descriptor.Descriptor(
  name='BroadcastMessage',
  full_name='atomicbroadcast.BroadcastMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Data', full_name='atomicbroadcast.BroadcastMessage.Data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=123,
)


_SEEKINFO = _descriptor.Descriptor(
  name='SeekInfo',
  full_name='atomicbroadcast.SeekInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Start', full_name='atomicbroadcast.SeekInfo.Start', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpecifiedNumber', full_name='atomicbroadcast.SeekInfo.SpecifiedNumber', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='WindowSize', full_name='atomicbroadcast.SeekInfo.WindowSize', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SEEKINFO_STARTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=285,
)


_ACKNOWLEDGEMENT = _descriptor.Descriptor(
  name='Acknowledgement',
  full_name='atomicbroadcast.Acknowledgement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Number', full_name='atomicbroadcast.Acknowledgement.Number', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=320,
)


_DELIVERUPDATE = _descriptor.Descriptor(
  name='DeliverUpdate',
  full_name='atomicbroadcast.DeliverUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Acknowledgement', full_name='atomicbroadcast.DeliverUpdate.Acknowledgement', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Seek', full_name='atomicbroadcast.DeliverUpdate.Seek', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='atomicbroadcast.DeliverUpdate.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=322,
  serialized_end=449,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='atomicbroadcast.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Number', full_name='atomicbroadcast.Block.Number', index=0,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PrevHash', full_name='atomicbroadcast.Block.PrevHash', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Proof', full_name='atomicbroadcast.Block.Proof', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Messages', full_name='atomicbroadcast.Block.Messages', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=560,
)


_DELIVERRESPONSE = _descriptor.Descriptor(
  name='DeliverResponse',
  full_name='atomicbroadcast.DeliverResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='atomicbroadcast.DeliverResponse.Error', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Block', full_name='atomicbroadcast.DeliverResponse.Block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='atomicbroadcast.DeliverResponse.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=562,
  serialized_end=670,
)

_BROADCASTRESPONSE.fields_by_name['Status'].enum_type = _STATUS
_SEEKINFO.fields_by_name['Start'].enum_type = _SEEKINFO_STARTTYPE
_SEEKINFO_STARTTYPE.containing_type = _SEEKINFO
_DELIVERUPDATE.fields_by_name['Acknowledgement'].message_type = _ACKNOWLEDGEMENT
_DELIVERUPDATE.fields_by_name['Seek'].message_type = _SEEKINFO
_DELIVERUPDATE.oneofs_by_name['Type'].fields.append(
  _DELIVERUPDATE.fields_by_name['Acknowledgement'])
_DELIVERUPDATE.fields_by_name['Acknowledgement'].containing_oneof = _DELIVERUPDATE.oneofs_by_name['Type']
_DELIVERUPDATE.oneofs_by_name['Type'].fields.append(
  _DELIVERUPDATE.fields_by_name['Seek'])
_DELIVERUPDATE.fields_by_name['Seek'].containing_oneof = _DELIVERUPDATE.oneofs_by_name['Type']
_BLOCK.fields_by_name['Messages'].message_type = _BROADCASTMESSAGE
_DELIVERRESPONSE.fields_by_name['Error'].enum_type = _STATUS
_DELIVERRESPONSE.fields_by_name['Block'].message_type = _BLOCK
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['Error'])
_DELIVERRESPONSE.fields_by_name['Error'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['Block'])
_DELIVERRESPONSE.fields_by_name['Block'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['BroadcastResponse'] = _BROADCASTRESPONSE
DESCRIPTOR.message_types_by_name['BroadcastMessage'] = _BROADCASTMESSAGE
DESCRIPTOR.message_types_by_name['SeekInfo'] = _SEEKINFO
DESCRIPTOR.message_types_by_name['Acknowledgement'] = _ACKNOWLEDGEMENT
DESCRIPTOR.message_types_by_name['DeliverUpdate'] = _DELIVERUPDATE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['DeliverResponse'] = _DELIVERRESPONSE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS

BroadcastResponse = _reflection.GeneratedProtocolMessageType('BroadcastResponse', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTRESPONSE,
  __module__ = 'ab_pb2'
  # @@protoc_insertion_point(class_scope:atomicbroadcast.BroadcastResponse)
  ))
_sym_db.RegisterMessage(BroadcastResponse)

BroadcastMessage = _reflection.GeneratedProtocolMessageType('BroadcastMessage', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTMESSAGE,
  __module__ = 'ab_pb2'
  # @@protoc_insertion_point(class_scope:atomicbroadcast.BroadcastMessage)
  ))
_sym_db.RegisterMessage(BroadcastMessage)

SeekInfo = _reflection.GeneratedProtocolMessageType('SeekInfo', (_message.Message,), dict(
  DESCRIPTOR = _SEEKINFO,
  __module__ = 'ab_pb2'
  # @@protoc_insertion_point(class_scope:atomicbroadcast.SeekInfo)
  ))
_sym_db.RegisterMessage(SeekInfo)

Acknowledgement = _reflection.GeneratedProtocolMessageType('Acknowledgement', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEMENT,
  __module__ = 'ab_pb2'
  # @@protoc_insertion_point(class_scope:atomicbroadcast.Acknowledgement)
  ))
_sym_db.RegisterMessage(Acknowledgement)

DeliverUpdate = _reflection.GeneratedProtocolMessageType('DeliverUpdate', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERUPDATE,
  __module__ = 'ab_pb2'
  # @@protoc_insertion_point(class_scope:atomicbroadcast.DeliverUpdate)
  ))
_sym_db.RegisterMessage(DeliverUpdate)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'ab_pb2'
  # @@protoc_insertion_point(class_scope:atomicbroadcast.Block)
  ))
_sym_db.RegisterMessage(Block)

DeliverResponse = _reflection.GeneratedProtocolMessageType('DeliverResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERRESPONSE,
  __module__ = 'ab_pb2'
  # @@protoc_insertion_point(class_scope:atomicbroadcast.DeliverResponse)
  ))
_sym_db.RegisterMessage(DeliverResponse)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class AtomicBroadcastStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Broadcast = channel.stream_stream(
        '/atomicbroadcast.AtomicBroadcast/Broadcast',
        request_serializer=BroadcastMessage.SerializeToString,
        response_deserializer=BroadcastResponse.FromString,
        )
    self.Deliver = channel.stream_stream(
        '/atomicbroadcast.AtomicBroadcast/Deliver',
        request_serializer=DeliverUpdate.SerializeToString,
        response_deserializer=DeliverResponse.FromString,
        )


class AtomicBroadcastServicer(object):

  def Broadcast(self, request_iterator, context):
    """broadcast receives a reply of Acknowledgement for each BroadcastMessage in order, indicating success or type of failure
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Deliver(self, request_iterator, context):
    """deliver first requires an update containing a seek message, then a stream of block replies is received.
    The receiver may choose to send an Acknowledgement for any block number it receives, however Acknowledgements must never be more than WindowSize apart
    To avoid latency, clients will likely acknowledge before the WindowSize has been exhausted, preventing the server from stopping and waiting for an Acknowledgement
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AtomicBroadcastServicer_to_server(servicer, server):
  """
  Adds AtomicBroadcastServicer methods to a gRPC server.
  Args:
      servicer: AtomicBroadcastServicer: The servicer to add
      server: grpc.Server: The server to add methods to
  Returns:
      None: No return value
  Adds the 'Broadcast' and 'Deliver' methods from the servicer to the server to handle AtomicBroadcast RPCs. Registers handlers for each method that handle serialization/deserialization of requests and responses.
  """
  
  rpc_method_handlers = {
      'Broadcast': grpc.stream_stream_rpc_method_handler(
          servicer.Broadcast,
          request_deserializer=BroadcastMessage.FromString,
          response_serializer=BroadcastResponse.SerializeToString,
      ),
      'Deliver': grpc.stream_stream_rpc_method_handler(
          servicer.Deliver,
          request_deserializer=DeliverUpdate.FromString,
          response_serializer=DeliverResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'atomicbroadcast.AtomicBroadcast', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaAtomicBroadcastServicer(object):
  def Broadcast(self, request_iterator, context):
    """broadcast receives a reply of Acknowledgement for each BroadcastMessage in order, indicating success or type of failure
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Deliver(self, request_iterator, context):
    """deliver first requires an update containing a seek message, then a stream of block replies is received.
    The receiver may choose to send an Acknowledgement for any block number it receives, however Acknowledgements must never be more than WindowSize apart
    To avoid latency, clients will likely acknowledge before the WindowSize has been exhausted, preventing the server from stopping and waiting for an Acknowledgement
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaAtomicBroadcastStub(object):
  def Broadcast(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    """broadcast receives a reply of Acknowledgement for each BroadcastMessage in order, indicating success or type of failure
    """
    raise NotImplementedError()
  def Deliver(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    """deliver first requires an update containing a seek message, then a stream of block replies is received.
    The receiver may choose to send an Acknowledgement for any block number it receives, however Acknowledgements must never be more than WindowSize apart
    To avoid latency, clients will likely acknowledge before the WindowSize has been exhausted, preventing the server from stopping and waiting for an Acknowledgement
    """
    raise NotImplementedError()


def beta_create_AtomicBroadcast_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """
  Creates an AtomicBroadcast server.
  Args:
      servicer: The AtomicBroadcast servicer.
      pool: The thread pool to use for asynchronous execution.
      pool_size: The thread pool size if no pool is provided.
      default_timeout: The default timeout for requests.
      maximum_timeout: The maximum timeout allowed for requests.
  Returns:
      server: A server object for the AtomicBroadcast service.
  Processing Logic:
      - Defines request and response serializers for Broadcast and Deliver methods
      - Defines method implementations that call corresponding methods on servicer
      - Creates server options with serializers, thread pool, timeouts
      - Returns a server object using options and method implementations
  """
  
  request_deserializers = {
    ('atomicbroadcast.AtomicBroadcast', 'Broadcast'): BroadcastMessage.FromString,
    ('atomicbroadcast.AtomicBroadcast', 'Deliver'): DeliverUpdate.FromString,
  }
  response_serializers = {
    ('atomicbroadcast.AtomicBroadcast', 'Broadcast'): BroadcastResponse.SerializeToString,
    ('atomicbroadcast.AtomicBroadcast', 'Deliver'): DeliverResponse.SerializeToString,
  }
  method_implementations = {
    ('atomicbroadcast.AtomicBroadcast', 'Broadcast'): face_utilities.stream_stream_inline(servicer.Broadcast),
    ('atomicbroadcast.AtomicBroadcast', 'Deliver'): face_utilities.stream_stream_inline(servicer.Deliver),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_AtomicBroadcast_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """
  Creates a gRPC stub for the AtomicBroadcast service.
  Args:
      channel: The gRPC channel
      host: The hostname to connect to
      metadata_transformer: A function to transform metadata
      pool: A thread pool for making calls
      pool_size: The size of the thread pool
  Returns:
      stub: A AtomicBroadcast stub
  - Serializes request and deserializes response for Broadcast and Deliver methods
  - Sets cardinality for Broadcast and Deliver methods
  - Creates dynamic stub with options like host, metadata transformer, thread pool
  - Returns the AtomicBroadcast stub
  """
  
  request_serializers = {
    ('atomicbroadcast.AtomicBroadcast', 'Broadcast'): BroadcastMessage.SerializeToString,
    ('atomicbroadcast.AtomicBroadcast', 'Deliver'): DeliverUpdate.SerializeToString,
  }
  response_deserializers = {
    ('atomicbroadcast.AtomicBroadcast', 'Broadcast'): BroadcastResponse.FromString,
    ('atomicbroadcast.AtomicBroadcast', 'Deliver'): DeliverResponse.FromString,
  }
  cardinalities = {
    'Broadcast': cardinality.Cardinality.STREAM_STREAM,
    'Deliver': cardinality.Cardinality.STREAM_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'atomicbroadcast.AtomicBroadcast', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
