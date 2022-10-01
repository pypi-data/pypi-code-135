"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....osmosis.streamswap.v1 import state_pb2 as osmosis_dot_streamswap_dot_v1_dot_state__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!osmosis/streamswap/v1/query.proto\x12\x15osmosis.streamswap.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a!osmosis/streamswap/v1/state.proto"H\n\nQuerySales\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x83\x01\n\x12QuerySalesResponse\x120\n\x05sales\x18\x01 \x03(\x0b2\x1b.osmosis.streamswap.v1.SaleB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x1c\n\tQuerySale\x12\x0f\n\x07sale_id\x18\x01 \x01(\x04"D\n\x11QuerySaleResponse\x12/\n\x04sale\x18\x01 \x01(\x0b2\x1b.osmosis.streamswap.v1.SaleB\x04\xc8\xde\x1f\x00"2\n\x11QueryUserPosition\x12\x0f\n\x07sale_id\x18\x01 \x01(\x04\x12\x0c\n\x04user\x18\x02 \x01(\t"]\n\x19QueryUserPositionResponse\x12@\n\ruser_position\x18\x01 \x01(\x0b2#.osmosis.streamswap.v1.UserPositionB\x04\xc8\xde\x1f\x002\xaa\x03\n\x05Query\x12z\n\x05Sales\x12!.osmosis.streamswap.v1.QuerySales\x1a).osmosis.streamswap.v1.QuerySalesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/streamswap/v1/sales\x12\x81\x01\n\x04Sale\x12 .osmosis.streamswap.v1.QuerySale\x1a(.osmosis.streamswap.v1.QuerySaleResponse"-\x82\xd3\xe4\x93\x02\'\x12%/cosmos/streamswap/v1/sales/{sale_id}\x12\xa0\x01\n\x0cUserPosition\x12(.osmosis.streamswap.v1.QueryUserPosition\x1a0.osmosis.streamswap.v1.QueryUserPositionResponse"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/streamswap/v1/sales/{sale_id}/{user}B<Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00b\x06proto3')
_QUERYSALES = DESCRIPTOR.message_types_by_name['QuerySales']
_QUERYSALESRESPONSE = DESCRIPTOR.message_types_by_name['QuerySalesResponse']
_QUERYSALE = DESCRIPTOR.message_types_by_name['QuerySale']
_QUERYSALERESPONSE = DESCRIPTOR.message_types_by_name['QuerySaleResponse']
_QUERYUSERPOSITION = DESCRIPTOR.message_types_by_name['QueryUserPosition']
_QUERYUSERPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryUserPositionResponse']
QuerySales = _reflection.GeneratedProtocolMessageType('QuerySales', (_message.Message,), {'DESCRIPTOR': _QUERYSALES, '__module__': 'osmosis.streamswap.v1.query_pb2'})
_sym_db.RegisterMessage(QuerySales)
QuerySalesResponse = _reflection.GeneratedProtocolMessageType('QuerySalesResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSALESRESPONSE, '__module__': 'osmosis.streamswap.v1.query_pb2'})
_sym_db.RegisterMessage(QuerySalesResponse)
QuerySale = _reflection.GeneratedProtocolMessageType('QuerySale', (_message.Message,), {'DESCRIPTOR': _QUERYSALE, '__module__': 'osmosis.streamswap.v1.query_pb2'})
_sym_db.RegisterMessage(QuerySale)
QuerySaleResponse = _reflection.GeneratedProtocolMessageType('QuerySaleResponse', (_message.Message,), {'DESCRIPTOR': _QUERYSALERESPONSE, '__module__': 'osmosis.streamswap.v1.query_pb2'})
_sym_db.RegisterMessage(QuerySaleResponse)
QueryUserPosition = _reflection.GeneratedProtocolMessageType('QueryUserPosition', (_message.Message,), {'DESCRIPTOR': _QUERYUSERPOSITION, '__module__': 'osmosis.streamswap.v1.query_pb2'})
_sym_db.RegisterMessage(QueryUserPosition)
QueryUserPositionResponse = _reflection.GeneratedProtocolMessageType('QueryUserPositionResponse', (_message.Message,), {'DESCRIPTOR': _QUERYUSERPOSITIONRESPONSE, '__module__': 'osmosis.streamswap.v1.query_pb2'})
_sym_db.RegisterMessage(QueryUserPositionResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v12/x/streamswap/types\xc8\xe1\x1e\x00'
    _QUERYSALESRESPONSE.fields_by_name['sales']._options = None
    _QUERYSALESRESPONSE.fields_by_name['sales']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYSALERESPONSE.fields_by_name['sale']._options = None
    _QUERYSALERESPONSE.fields_by_name['sale']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYUSERPOSITIONRESPONSE.fields_by_name['user_position']._options = None
    _QUERYUSERPOSITIONRESPONSE.fields_by_name['user_position']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Sales']._options = None
    _QUERY.methods_by_name['Sales']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/streamswap/v1/sales'
    _QUERY.methods_by_name['Sale']._options = None
    _QUERY.methods_by_name['Sale']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/cosmos/streamswap/v1/sales/{sale_id}"
    _QUERY.methods_by_name['UserPosition']._options = None
    _QUERY.methods_by_name['UserPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/cosmos/streamswap/v1/sales/{sale_id}/{user}'
    _QUERYSALES._serialized_start = 191
    _QUERYSALES._serialized_end = 263
    _QUERYSALESRESPONSE._serialized_start = 266
    _QUERYSALESRESPONSE._serialized_end = 397
    _QUERYSALE._serialized_start = 399
    _QUERYSALE._serialized_end = 427
    _QUERYSALERESPONSE._serialized_start = 429
    _QUERYSALERESPONSE._serialized_end = 497
    _QUERYUSERPOSITION._serialized_start = 499
    _QUERYUSERPOSITION._serialized_end = 549
    _QUERYUSERPOSITIONRESPONSE._serialized_start = 551
    _QUERYUSERPOSITIONRESPONSE._serialized_end = 644
    _QUERY._serialized_start = 647
    _QUERY._serialized_end = 1073