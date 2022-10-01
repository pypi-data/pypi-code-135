# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: android_checkin.proto

import sys

from google.protobuf import (
    descriptor as _descriptor,
    message as _message,
    reflection as _reflection,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import enum_type_wrapper

_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='android_checkin.proto',
    package='checkin_proto',
    syntax='proto2',
    serialized_options=_b('H\003'),
    serialized_pb=_b('\n\x15\x61ndroid_checkin.proto\x12\rcheckin_proto\"\x8a\x03\n\x10\x43hromeBuildProto\x12:\n\x08platform\x18\x01 \x01(\x0e\x32(.checkin_proto.ChromeBuildProto.Platform\x12\x16\n\x0e\x63hrome_version\x18\x02 \x01(\t\x12\x38\n\x07\x63hannel\x18\x03 \x01(\x0e\x32\'.checkin_proto.ChromeBuildProto.Channel\"}\n\x08Platform\x12\x10\n\x0cPLATFORM_WIN\x10\x01\x12\x10\n\x0cPLATFORM_MAC\x10\x02\x12\x12\n\x0ePLATFORM_LINUX\x10\x03\x12\x11\n\rPLATFORM_CROS\x10\x04\x12\x10\n\x0cPLATFORM_IOS\x10\x05\x12\x14\n\x10PLATFORM_ANDROID\x10\x06\"i\n\x07\x43hannel\x12\x12\n\x0e\x43HANNEL_STABLE\x10\x01\x12\x10\n\x0c\x43HANNEL_BETA\x10\x02\x12\x0f\n\x0b\x43HANNEL_DEV\x10\x03\x12\x12\n\x0e\x43HANNEL_CANARY\x10\x04\x12\x13\n\x0f\x43HANNEL_UNKNOWN\x10\x05\"\xf6\x01\n\x13\x41ndroidCheckinProto\x12\x19\n\x11last_checkin_msec\x18\x02 \x01(\x03\x12\x15\n\rcell_operator\x18\x06 \x01(\t\x12\x14\n\x0csim_operator\x18\x07 \x01(\t\x12\x0f\n\x07roaming\x18\x08 \x01(\t\x12\x13\n\x0buser_number\x18\t \x01(\x05\x12:\n\x04type\x18\x0c \x01(\x0e\x32\x19.checkin_proto.DeviceType:\x11\x44\x45VICE_ANDROID_OS\x12\x35\n\x0c\x63hrome_build\x18\r \x01(\x0b\x32\x1f.checkin_proto.ChromeBuildProto*g\n\nDeviceType\x12\x15\n\x11\x44\x45VICE_ANDROID_OS\x10\x01\x12\x11\n\rDEVICE_IOS_OS\x10\x02\x12\x19\n\x15\x44\x45VICE_CHROME_BROWSER\x10\x03\x12\x14\n\x10\x44\x45VICE_CHROME_OS\x10\x04\x42\x02H\x03')
)

_DEVICETYPE = _descriptor.EnumDescriptor(
    name='DeviceType',
    full_name='checkin_proto.DeviceType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='DEVICE_ANDROID_OS', index=0, number=1,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DEVICE_IOS_OS', index=1, number=2,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DEVICE_CHROME_BROWSER', index=2, number=3,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DEVICE_CHROME_OS', index=3, number=4,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=686,
    serialized_end=789,
)
_sym_db.RegisterEnumDescriptor(_DEVICETYPE)

DeviceType = enum_type_wrapper.EnumTypeWrapper(_DEVICETYPE)
DEVICE_ANDROID_OS = 1
DEVICE_IOS_OS = 2
DEVICE_CHROME_BROWSER = 3
DEVICE_CHROME_OS = 4


_CHROMEBUILDPROTO_PLATFORM = _descriptor.EnumDescriptor(
    name='Platform',
    full_name='checkin_proto.ChromeBuildProto.Platform',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='PLATFORM_WIN', index=0, number=1,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PLATFORM_MAC', index=1, number=2,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PLATFORM_LINUX', index=2, number=3,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PLATFORM_CROS', index=3, number=4,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PLATFORM_IOS', index=4, number=5,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PLATFORM_ANDROID', index=5, number=6,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=203,
    serialized_end=328,
)
_sym_db.RegisterEnumDescriptor(_CHROMEBUILDPROTO_PLATFORM)

_CHROMEBUILDPROTO_CHANNEL = _descriptor.EnumDescriptor(
    name='Channel',
    full_name='checkin_proto.ChromeBuildProto.Channel',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='CHANNEL_STABLE', index=0, number=1,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CHANNEL_BETA', index=1, number=2,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CHANNEL_DEV', index=2, number=3,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CHANNEL_CANARY', index=3, number=4,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CHANNEL_UNKNOWN', index=4, number=5,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=330,
    serialized_end=435,
)
_sym_db.RegisterEnumDescriptor(_CHROMEBUILDPROTO_CHANNEL)


_CHROMEBUILDPROTO = _descriptor.Descriptor(
    name='ChromeBuildProto',
    full_name='checkin_proto.ChromeBuildProto',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='platform', full_name='checkin_proto.ChromeBuildProto.platform', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='chrome_version', full_name='checkin_proto.ChromeBuildProto.chrome_version', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='channel', full_name='checkin_proto.ChromeBuildProto.channel', index=2,
            number=3, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _CHROMEBUILDPROTO_PLATFORM,
        _CHROMEBUILDPROTO_CHANNEL,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=41,
    serialized_end=435,
)


_ANDROIDCHECKINPROTO = _descriptor.Descriptor(
    name='AndroidCheckinProto',
    full_name='checkin_proto.AndroidCheckinProto',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='last_checkin_msec', full_name='checkin_proto.AndroidCheckinProto.last_checkin_msec', index=0,
            number=2, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cell_operator', full_name='checkin_proto.AndroidCheckinProto.cell_operator', index=1,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sim_operator', full_name='checkin_proto.AndroidCheckinProto.sim_operator', index=2,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='roaming', full_name='checkin_proto.AndroidCheckinProto.roaming', index=3,
            number=8, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='user_number', full_name='checkin_proto.AndroidCheckinProto.user_number', index=4,
            number=9, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='type', full_name='checkin_proto.AndroidCheckinProto.type', index=5,
            number=12, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='chrome_build', full_name='checkin_proto.AndroidCheckinProto.chrome_build', index=6,
            number=13, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=438,
    serialized_end=684,
)

_CHROMEBUILDPROTO.fields_by_name['platform'].enum_type = _CHROMEBUILDPROTO_PLATFORM
_CHROMEBUILDPROTO.fields_by_name['channel'].enum_type = _CHROMEBUILDPROTO_CHANNEL
_CHROMEBUILDPROTO_PLATFORM.containing_type = _CHROMEBUILDPROTO
_CHROMEBUILDPROTO_CHANNEL.containing_type = _CHROMEBUILDPROTO
_ANDROIDCHECKINPROTO.fields_by_name['type'].enum_type = _DEVICETYPE
_ANDROIDCHECKINPROTO.fields_by_name['chrome_build'].message_type = _CHROMEBUILDPROTO
DESCRIPTOR.message_types_by_name['ChromeBuildProto'] = _CHROMEBUILDPROTO
DESCRIPTOR.message_types_by_name['AndroidCheckinProto'] = _ANDROIDCHECKINPROTO
DESCRIPTOR.enum_types_by_name['DeviceType'] = _DEVICETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChromeBuildProto = _reflection.GeneratedProtocolMessageType('ChromeBuildProto', (_message.Message,), dict(
    DESCRIPTOR=_CHROMEBUILDPROTO,
    __module__='android_checkin_pb2'
    # @@protoc_insertion_point(class_scope:checkin_proto.ChromeBuildProto)
))
_sym_db.RegisterMessage(ChromeBuildProto)

AndroidCheckinProto = _reflection.GeneratedProtocolMessageType('AndroidCheckinProto', (_message.Message,), dict(
    DESCRIPTOR=_ANDROIDCHECKINPROTO,
    __module__='android_checkin_pb2'
    # @@protoc_insertion_point(class_scope:checkin_proto.AndroidCheckinProto)
))
_sym_db.RegisterMessage(AndroidCheckinProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
