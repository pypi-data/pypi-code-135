"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!osmosis/streamswap/v1/event.proto\x12\x15osmosis.streamswap.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto"t\n\x0fEventCreateSale\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07creator\x18\x02 \x01(\t\x12\x10\n\x08token_in\x18\x03 \x01(\t\x122\n\ttoken_out\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"A\n\x0eEventSubscribe\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07sale_id\x18\x02 \x01(\x04\x12\x0e\n\x06amount\x18\x03 \x01(\t"@\n\rEventWithdraw\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07sale_id\x18\x02 \x01(\x04\x12\x0e\n\x06amount\x18\x03 \x01(\t"?\n\tEventExit\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07sale_id\x18\x02 \x01(\x04\x12\x11\n\tpurchased\x18\x03 \x01(\t"4\n\x11EventFinalizeSale\x12\x0f\n\x07sale_id\x18\x01 \x01(\x04\x12\x0e\n\x06income\x18\x03 \x01(\tB<Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00b\x06proto3')
_EVENTCREATESALE = DESCRIPTOR.message_types_by_name['EventCreateSale']
_EVENTSUBSCRIBE = DESCRIPTOR.message_types_by_name['EventSubscribe']
_EVENTWITHDRAW = DESCRIPTOR.message_types_by_name['EventWithdraw']
_EVENTEXIT = DESCRIPTOR.message_types_by_name['EventExit']
_EVENTFINALIZESALE = DESCRIPTOR.message_types_by_name['EventFinalizeSale']
EventCreateSale = _reflection.GeneratedProtocolMessageType('EventCreateSale', (_message.Message,), {'DESCRIPTOR': _EVENTCREATESALE, '__module__': 'osmosis.streamswap.v1.event_pb2'})
_sym_db.RegisterMessage(EventCreateSale)
EventSubscribe = _reflection.GeneratedProtocolMessageType('EventSubscribe', (_message.Message,), {'DESCRIPTOR': _EVENTSUBSCRIBE, '__module__': 'osmosis.streamswap.v1.event_pb2'})
_sym_db.RegisterMessage(EventSubscribe)
EventWithdraw = _reflection.GeneratedProtocolMessageType('EventWithdraw', (_message.Message,), {'DESCRIPTOR': _EVENTWITHDRAW, '__module__': 'osmosis.streamswap.v1.event_pb2'})
_sym_db.RegisterMessage(EventWithdraw)
EventExit = _reflection.GeneratedProtocolMessageType('EventExit', (_message.Message,), {'DESCRIPTOR': _EVENTEXIT, '__module__': 'osmosis.streamswap.v1.event_pb2'})
_sym_db.RegisterMessage(EventExit)
EventFinalizeSale = _reflection.GeneratedProtocolMessageType('EventFinalizeSale', (_message.Message,), {'DESCRIPTOR': _EVENTFINALIZESALE, '__module__': 'osmosis.streamswap.v1.event_pb2'})
_sym_db.RegisterMessage(EventFinalizeSale)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00'
    _EVENTCREATESALE.fields_by_name['token_out']._options = None
    _EVENTCREATESALE.fields_by_name['token_out']._serialized_options = b'\xc8\xde\x1f\x00'
    _EVENTCREATESALE._serialized_start = 141
    _EVENTCREATESALE._serialized_end = 257
    _EVENTSUBSCRIBE._serialized_start = 259
    _EVENTSUBSCRIBE._serialized_end = 324
    _EVENTWITHDRAW._serialized_start = 326
    _EVENTWITHDRAW._serialized_end = 390
    _EVENTEXIT._serialized_start = 392
    _EVENTEXIT._serialized_end = 455
    _EVENTFINALIZESALE._serialized_start = 457
    _EVENTFINALIZESALE._serialized_end = 509