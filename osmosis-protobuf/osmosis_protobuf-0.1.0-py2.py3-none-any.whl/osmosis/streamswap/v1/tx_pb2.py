"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/streamswap/v1/tx.proto\x12\x15osmosis.streamswap.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19cosmos_proto/cosmos.proto"\xb7\x02\n\rMsgCreateSale\x12\x0f\n\x07creator\x18\x01 \x01(\t\x12\x10\n\x08token_in\x18\x02 \x01(\t\x122\n\ttoken_out\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x120\n\x07max_fee\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x128\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x125\n\x08duration\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x11\n\trecipient\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\t \x01(\t"<\n\x15MsgCreateSaleResponse\x12#\n\x07sale_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"sale_id""\x83\x01\n\x0cMsgSubscribe\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12#\n\x07sale_id\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"sale_id"\x12>\n\x06amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"\x82\x01\n\x0bMsgWithdraw\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12#\n\x07sale_id\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"sale_id"\x12>\n\x06amount\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01"B\n\x0bMsgExitSale\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12#\n\x07sale_id\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"sale_id""X\n\x13MsgExitSaleResponse\x12A\n\tpurchased\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"F\n\x0fMsgFinalizeSale\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12#\n\x07sale_id\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"sale_id""Y\n\x17MsgFinalizeSaleResponse\x12>\n\x06income\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x002\xbd\x03\n\x03Msg\x12`\n\nCreateSale\x12$.osmosis.streamswap.v1.MsgCreateSale\x1a,.osmosis.streamswap.v1.MsgCreateSaleResponse\x12H\n\tSubscribe\x12#.osmosis.streamswap.v1.MsgSubscribe\x1a\x16.google.protobuf.Empty\x12F\n\x08Withdraw\x12".osmosis.streamswap.v1.MsgWithdraw\x1a\x16.google.protobuf.Empty\x12Z\n\x08ExitSale\x12".osmosis.streamswap.v1.MsgExitSale\x1a*.osmosis.streamswap.v1.MsgExitSaleResponse\x12f\n\x0cFinalizeSale\x12&.osmosis.streamswap.v1.MsgFinalizeSale\x1a..osmosis.streamswap.v1.MsgFinalizeSaleResponseB<Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00b\x06proto3')
_MSGCREATESALE = DESCRIPTOR.message_types_by_name['MsgCreateSale']
_MSGCREATESALERESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateSaleResponse']
_MSGSUBSCRIBE = DESCRIPTOR.message_types_by_name['MsgSubscribe']
_MSGWITHDRAW = DESCRIPTOR.message_types_by_name['MsgWithdraw']
_MSGEXITSALE = DESCRIPTOR.message_types_by_name['MsgExitSale']
_MSGEXITSALERESPONSE = DESCRIPTOR.message_types_by_name['MsgExitSaleResponse']
_MSGFINALIZESALE = DESCRIPTOR.message_types_by_name['MsgFinalizeSale']
_MSGFINALIZESALERESPONSE = DESCRIPTOR.message_types_by_name['MsgFinalizeSaleResponse']
MsgCreateSale = _reflection.GeneratedProtocolMessageType('MsgCreateSale', (_message.Message,), {'DESCRIPTOR': _MSGCREATESALE, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateSale)
MsgCreateSaleResponse = _reflection.GeneratedProtocolMessageType('MsgCreateSaleResponse', (_message.Message,), {'DESCRIPTOR': _MSGCREATESALERESPONSE, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgCreateSaleResponse)
MsgSubscribe = _reflection.GeneratedProtocolMessageType('MsgSubscribe', (_message.Message,), {'DESCRIPTOR': _MSGSUBSCRIBE, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgSubscribe)
MsgWithdraw = _reflection.GeneratedProtocolMessageType('MsgWithdraw', (_message.Message,), {'DESCRIPTOR': _MSGWITHDRAW, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgWithdraw)
MsgExitSale = _reflection.GeneratedProtocolMessageType('MsgExitSale', (_message.Message,), {'DESCRIPTOR': _MSGEXITSALE, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitSale)
MsgExitSaleResponse = _reflection.GeneratedProtocolMessageType('MsgExitSaleResponse', (_message.Message,), {'DESCRIPTOR': _MSGEXITSALERESPONSE, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgExitSaleResponse)
MsgFinalizeSale = _reflection.GeneratedProtocolMessageType('MsgFinalizeSale', (_message.Message,), {'DESCRIPTOR': _MSGFINALIZESALE, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgFinalizeSale)
MsgFinalizeSaleResponse = _reflection.GeneratedProtocolMessageType('MsgFinalizeSaleResponse', (_message.Message,), {'DESCRIPTOR': _MSGFINALIZESALERESPONSE, '__module__': 'osmosis.streamswap.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgFinalizeSaleResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00'
    _MSGCREATESALE.fields_by_name['token_out']._options = None
    _MSGCREATESALE.fields_by_name['token_out']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATESALE.fields_by_name['max_fee']._options = None
    _MSGCREATESALE.fields_by_name['max_fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATESALE.fields_by_name['start_time']._options = None
    _MSGCREATESALE.fields_by_name['start_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _MSGCREATESALE.fields_by_name['duration']._options = None
    _MSGCREATESALE.fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _MSGCREATESALERESPONSE.fields_by_name['sale_id']._options = None
    _MSGCREATESALERESPONSE.fields_by_name['sale_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"sale_id"'
    _MSGSUBSCRIBE.fields_by_name['sale_id']._options = None
    _MSGSUBSCRIBE.fields_by_name['sale_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"sale_id"'
    _MSGSUBSCRIBE.fields_by_name['amount']._options = None
    _MSGSUBSCRIBE.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MSGWITHDRAW.fields_by_name['sale_id']._options = None
    _MSGWITHDRAW.fields_by_name['sale_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"sale_id"'
    _MSGWITHDRAW.fields_by_name['amount']._options = None
    _MSGWITHDRAW.fields_by_name['amount']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x01'
    _MSGEXITSALE.fields_by_name['sale_id']._options = None
    _MSGEXITSALE.fields_by_name['sale_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"sale_id"'
    _MSGEXITSALERESPONSE.fields_by_name['purchased']._options = None
    _MSGEXITSALERESPONSE.fields_by_name['purchased']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MSGFINALIZESALE.fields_by_name['sale_id']._options = None
    _MSGFINALIZESALE.fields_by_name['sale_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"sale_id"'
    _MSGFINALIZESALERESPONSE.fields_by_name['income']._options = None
    _MSGFINALIZESALERESPONSE.fields_by_name['income']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _MSGCREATESALE._serialized_start = 233
    _MSGCREATESALE._serialized_end = 544
    _MSGCREATESALERESPONSE._serialized_start = 546
    _MSGCREATESALERESPONSE._serialized_end = 606
    _MSGSUBSCRIBE._serialized_start = 609
    _MSGSUBSCRIBE._serialized_end = 740
    _MSGWITHDRAW._serialized_start = 743
    _MSGWITHDRAW._serialized_end = 873
    _MSGEXITSALE._serialized_start = 875
    _MSGEXITSALE._serialized_end = 941
    _MSGEXITSALERESPONSE._serialized_start = 943
    _MSGEXITSALERESPONSE._serialized_end = 1031
    _MSGFINALIZESALE._serialized_start = 1033
    _MSGFINALIZESALE._serialized_end = 1103
    _MSGFINALIZESALERESPONSE._serialized_start = 1105
    _MSGFINALIZESALERESPONSE._serialized_end = 1194
    _MSG._serialized_start = 1197
    _MSG._serialized_end = 1642