# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/types/Field.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.protos.feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66\x65\x61st/types/Field.proto\x12\x0b\x66\x65\x61st.types\x1a\x17\x66\x65\x61st/types/Value.proto\"A\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0e\x32\x1b.feast.types.ValueType.EnumBQ\n\x11\x66\x65\x61st.proto.typesB\nFieldProtoZ0github.com/feast-dev/feast/go/protos/feast/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.types.Field_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021feast.proto.typesB\nFieldProtoZ0github.com/feast-dev/feast/go/protos/feast/types'
  _FIELD._serialized_start=65
  _FIELD._serialized_end=130
# @@protoc_insertion_point(module_scope)
