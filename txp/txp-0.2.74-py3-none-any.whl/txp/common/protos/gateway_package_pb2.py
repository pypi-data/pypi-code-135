# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway_package.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import txp.common.protos.gateway_config_pb2 as gateway__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15gateway_package.proto\x1a\x14gateway_config.proto\".\n\x1b\x44imensionSignalSamplesProto\x12\x0f\n\x07samples\x18\x01 \x03(\x02\"\xd8\x01\n\x0bSignalProto\x12-\n\x07samples\x18\x01 \x03(\x0b\x32\x1c.DimensionSignalSamplesProto\x12\x17\n\x0fperception_name\x18\x02 \x01(\t\x12\x1d\n\x15perception_dimensions\x18\x03 \x03(\x05\x12\x1d\n\x10signal_frequency\x18\x04 \x01(\x02H\x00\x88\x01\x01\x12\x1b\n\x13sampling_resolution\x18\x05 \x01(\x05\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x42\x13\n\x11_signal_frequency\"\xbf\x01\n\x1bGatewayPackageMetadataProto\x12-\n\x0f\x65\x64ge_descriptor\x18\x01 \x01(\x0b\x32\x14.EdgeDescriptorProto\x12-\n\x0fsampling_window\x18\x02 \x01(\x0b\x32\x14.SamplingWindowProto\x12\x12\n\npackage_id\x18\x03 \x01(\t\x12\x1b\n\x13previous_part_index\x18\x04 \x01(\x05\x12\x11\n\ttenant_id\x18\x0b \x01(\t\"~\n\x13GatewayPackageProto\x12.\n\x08metadata\x18\x01 \x01(\x0b\x32\x1c.GatewayPackageMetadataProto\x12\x1d\n\x07signals\x18\x02 \x03(\x0b\x32\x0c.SignalProto\x12\x18\n\x10\x63onfiguration_id\x18\x03 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway_package_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DIMENSIONSIGNALSAMPLESPROTO._serialized_start=47
  _DIMENSIONSIGNALSAMPLESPROTO._serialized_end=93
  _SIGNALPROTO._serialized_start=96
  _SIGNALPROTO._serialized_end=312
  _GATEWAYPACKAGEMETADATAPROTO._serialized_start=315
  _GATEWAYPACKAGEMETADATAPROTO._serialized_end=506
  _GATEWAYPACKAGEPROTO._serialized_start=508
  _GATEWAYPACKAGEPROTO._serialized_end=634
# @@protoc_insertion_point(module_scope)
