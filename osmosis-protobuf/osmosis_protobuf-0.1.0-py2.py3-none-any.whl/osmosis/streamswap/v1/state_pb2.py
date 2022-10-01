"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!osmosis/streamswap/v1/state.proto\x12\x15osmosis.streamswap.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto"\xd2\x05\n\x04Sale\x12\x10\n\x08treasury\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x11\n\ttoken_out\x18\x03 \x01(\t\x12\x10\n\x08token_in\x18\x04 \x01(\t\x12H\n\x10token_out_supply\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x128\n\nstart_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x126\n\x08end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\r\n\x05round\x18\x08 \x01(\x03\x12\x11\n\tend_round\x18\t \x01(\x03\x12E\n\rout_remaining\x18\n \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12@\n\x08out_sold\x18\x0b \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12E\n\rout_per_share\x18\x0c \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12>\n\x06staked\x18\r \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12>\n\x06income\x18\x0e \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12>\n\x06shares\x18\x0f \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x0c\n\x04name\x18\x14 \x01(\t\x12\x0b\n\x03url\x18\x15 \x01(\t"\xd7\x02\n\x0cUserPosition\x12>\n\x06shares\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12>\n\x06staked\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12E\n\rout_per_share\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12=\n\x05spent\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12A\n\tpurchased\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00B<Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00b\x06proto3')
_SALE = DESCRIPTOR.message_types_by_name['Sale']
_USERPOSITION = DESCRIPTOR.message_types_by_name['UserPosition']
Sale = _reflection.GeneratedProtocolMessageType('Sale', (_message.Message,), {'DESCRIPTOR': _SALE, '__module__': 'osmosis.streamswap.v1.state_pb2'})
_sym_db.RegisterMessage(Sale)
UserPosition = _reflection.GeneratedProtocolMessageType('UserPosition', (_message.Message,), {'DESCRIPTOR': _USERPOSITION, '__module__': 'osmosis.streamswap.v1.state_pb2'})
_sym_db.RegisterMessage(UserPosition)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00'
    _SALE.fields_by_name['token_out_supply']._options = None
    _SALE.fields_by_name['token_out_supply']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _SALE.fields_by_name['start_time']._options = None
    _SALE.fields_by_name['start_time']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00'
    _SALE.fields_by_name['end_time']._options = None
    _SALE.fields_by_name['end_time']._serialized_options = b'\x90\xdf\x1f\x01\xc8\xde\x1f\x00'
    _SALE.fields_by_name['out_remaining']._options = None
    _SALE.fields_by_name['out_remaining']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _SALE.fields_by_name['out_sold']._options = None
    _SALE.fields_by_name['out_sold']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _SALE.fields_by_name['out_per_share']._options = None
    _SALE.fields_by_name['out_per_share']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _SALE.fields_by_name['staked']._options = None
    _SALE.fields_by_name['staked']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _SALE.fields_by_name['income']._options = None
    _SALE.fields_by_name['income']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _SALE.fields_by_name['shares']._options = None
    _SALE.fields_by_name['shares']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _USERPOSITION.fields_by_name['shares']._options = None
    _USERPOSITION.fields_by_name['shares']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _USERPOSITION.fields_by_name['staked']._options = None
    _USERPOSITION.fields_by_name['staked']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _USERPOSITION.fields_by_name['out_per_share']._options = None
    _USERPOSITION.fields_by_name['out_per_share']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _USERPOSITION.fields_by_name['spent']._options = None
    _USERPOSITION.fields_by_name['spent']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _USERPOSITION.fields_by_name['purchased']._options = None
    _USERPOSITION.fields_by_name['purchased']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00'
    _SALE._serialized_start = 143
    _SALE._serialized_end = 865
    _USERPOSITION._serialized_start = 868
    _USERPOSITION._serialized_end = 1211