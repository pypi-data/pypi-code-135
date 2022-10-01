"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....osmosis.streamswap.v1 import state_pb2 as osmosis_dot_streamswap_dot_v1_dot_state__pb2
from ....osmosis.streamswap.v1 import params_pb2 as osmosis_dot_streamswap_dot_v1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#osmosis/streamswap/v1/genesis.proto\x12\x15osmosis.streamswap.v1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a!osmosis/streamswap/v1/state.proto\x1a"osmosis/streamswap/v1/params.proto"\xd0\x01\n\x0cGenesisState\x120\n\x05sales\x18\x01 \x03(\x0b2\x1b.osmosis.streamswap.v1.SaleB\x04\xc8\xde\x1f\x00\x12C\n\x0euser_positions\x18\x02 \x03(\x0b2%.osmosis.streamswap.v1.UserPositionKVB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cnext_sale_id\x18\x03 \x01(\x04\x123\n\x06params\x18\x04 \x01(\x0b2\x1d.osmosis.streamswap.v1.ParamsB\x04\xc8\xde\x1f\x00"x\n\x0eUserPositionKV\x12\x13\n\x0bacc_address\x18\x01 \x01(\t\x12\x0f\n\x07sale_id\x18\x02 \x01(\x04\x12@\n\ruser_position\x18\x03 \x01(\x0b2#.osmosis.streamswap.v1.UserPositionB\x04\xc8\xde\x1f\x00B8Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_USERPOSITIONKV = DESCRIPTOR.message_types_by_name['UserPositionKV']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'osmosis.streamswap.v1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
UserPositionKV = _reflection.GeneratedProtocolMessageType('UserPositionKV', (_message.Message,), {'DESCRIPTOR': _USERPOSITIONKV, '__module__': 'osmosis.streamswap.v1.genesis_pb2'})
_sym_db.RegisterMessage(UserPositionKV)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types'
    _GENESISSTATE.fields_by_name['sales']._options = None
    _GENESISSTATE.fields_by_name['sales']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['user_positions']._options = None
    _GENESISSTATE.fields_by_name['user_positions']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _USERPOSITIONKV.fields_by_name['user_position']._options = None
    _USERPOSITIONKV.fields_by_name['user_position']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 215
    _GENESISSTATE._serialized_end = 423
    _USERPOSITIONKV._serialized_start = 425
    _USERPOSITIONKV._serialized_end = 545