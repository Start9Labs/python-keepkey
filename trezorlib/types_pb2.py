# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='types.proto',
  package='',
  serialized_pb='\n\x0btypes.proto\x1a google/protobuf/descriptor.proto\"\x92\x01\n\nHDNodeType\x12\r\n\x05\x64\x65pth\x18\x01 \x02(\r\x12\x13\n\x0b\x66ingerprint\x18\x02 \x02(\r\x12\x11\n\tchild_num\x18\x03 \x02(\r\x12\x18\n\nchain_code\x18\x04 \x02(\x0c\x42\x04\x88\xb5\x18\x01\x12\x19\n\x0bprivate_key\x18\x05 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12\x18\n\npublic_key\x18\x06 \x01(\x0c\x42\x04\x88\xb5\x18\x01\"]\n\x08\x43oinType\x12\x11\n\tcoin_name\x18\x01 \x01(\x0c\x12\x15\n\rcoin_shortcut\x18\x02 \x01(\x0c\x12\x14\n\x0c\x61\x64\x64ress_type\x18\x03 \x01(\r\x12\x11\n\tmaxfee_kb\x18\x04 \x01(\x04\"\x85\x01\n\x0bTxInputType\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x17\n\tprev_hash\x18\x02 \x02(\x0c\x42\x04\x88\xb5\x18\x01\x12\x12\n\nprev_index\x18\x03 \x02(\r\x12\x18\n\nscript_sig\x18\x04 \x01(\x0c\x42\x04\x88\xb5\x18\x01\x12\x1c\n\x08sequence\x18\x05 \x01(\r:\n4294967295\"\x7f\n\x0cTxOutputType\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x11\n\taddress_n\x18\x02 \x03(\r\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x04\x12 \n\x0bscript_type\x18\x04 \x02(\x0e\x32\x0b.ScriptType\x12\x19\n\x0bscript_args\x18\x05 \x03(\x0c\x42\x04\x88\xb5\x18\x01\">\n\x0fTxOutputBinType\x12\x0e\n\x06\x61mount\x18\x01 \x02(\x04\x12\x1b\n\rscript_pubkey\x18\x02 \x02(\x0c\x42\x04\x88\xb5\x18\x01\"|\n\x0fTransactionType\x12\x12\n\x07version\x18\x01 \x01(\r:\x01\x31\x12\x1c\n\x06inputs\x18\x02 \x03(\x0b\x32\x0c.TxInputType\x12!\n\x07outputs\x18\x03 \x03(\x0b\x32\x10.TxOutputBinType\x12\x14\n\tlock_time\x18\x04 \x01(\r:\x01\x30*\xcd\x02\n\x0b\x46\x61ilureType\x12\x1d\n\x19\x46\x61ilure_UnexpectedMessage\x10\x01\x12\x1a\n\x16\x46\x61ilure_ButtonExpected\x10\x02\x12\x17\n\x13\x46\x61ilure_SyntaxError\x10\x03\x12\x1b\n\x17\x46\x61ilure_ActionCancelled\x10\x04\x12\x17\n\x13\x46\x61ilure_PinExpected\x10\x05\x12\x18\n\x14\x46\x61ilure_PinCancelled\x10\x06\x12\x16\n\x12\x46\x61ilure_PinInvalid\x10\x07\x12\x1c\n\x18\x46\x61ilure_InvalidSignature\x10\x08\x12\x11\n\rFailure_Other\x10\t\x12\x1a\n\x16\x46\x61ilure_NotEnoughFunds\x10\n\x12\x1a\n\x16\x46\x61ilure_NotInitialized\x10\x0b\x12\x19\n\x15\x46\x61ilure_FirmwareError\x10\x63*3\n\nScriptType\x12\x10\n\x0cPAYTOADDRESS\x10\x00\x12\x13\n\x0fPAYTOSCRIPTHASH\x10\x01*(\n\x0bRequestType\x12\x0b\n\x07TXINPUT\x10\x00\x12\x0c\n\x08TXOUTPUT\x10\x01*\x86\x02\n\x11\x42uttonRequestType\x12\x17\n\x13\x42uttonRequest_Other\x10\x01\x12\"\n\x1e\x42uttonRequest_FeeOverThreshold\x10\x02\x12\x1f\n\x1b\x42uttonRequest_ConfirmOutput\x10\x03\x12\x1d\n\x19\x42uttonRequest_ResetDevice\x10\x04\x12\x1d\n\x19\x42uttonRequest_ConfirmWord\x10\x05\x12\x1c\n\x18\x42uttonRequest_WipeDevice\x10\x06\x12\x1d\n\x19\x42uttonRequest_ProtectCall\x10\x07\x12\x18\n\x14\x42uttonRequest_SignTx\x10\x08:/\n\x06\x62inary\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x08:4\n\x07wire_in\x12!.google.protobuf.EnumValueOptions\x18\xd2\x86\x03 \x01(\x08:5\n\x08wire_out\x12!.google.protobuf.EnumValueOptions\x18\xd3\x86\x03 \x01(\x08::\n\rwire_debug_in\x12!.google.protobuf.EnumValueOptions\x18\xd4\x86\x03 \x01(\x08:;\n\x0ewire_debug_out\x12!.google.protobuf.EnumValueOptions\x18\xd5\x86\x03 \x01(\x08\x42\x36\n(org.multibit.hd.hardware.trezor.protobufB\nTrezorType')

_FAILURETYPE = _descriptor.EnumDescriptor(
  name='FailureType',
  full_name='FailureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Failure_UnexpectedMessage', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_ButtonExpected', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_SyntaxError', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_ActionCancelled', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_PinExpected', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_PinCancelled', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_PinInvalid', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_InvalidSignature', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_Other', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_NotEnoughFunds', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_NotInitialized', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failure_FirmwareError', index=11, number=99,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=749,
  serialized_end=1082,
)

FailureType = enum_type_wrapper.EnumTypeWrapper(_FAILURETYPE)
_SCRIPTTYPE = _descriptor.EnumDescriptor(
  name='ScriptType',
  full_name='ScriptType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAYTOADDRESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYTOSCRIPTHASH', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1084,
  serialized_end=1135,
)

ScriptType = enum_type_wrapper.EnumTypeWrapper(_SCRIPTTYPE)
_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TXINPUT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TXOUTPUT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1137,
  serialized_end=1177,
)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
_BUTTONREQUESTTYPE = _descriptor.EnumDescriptor(
  name='ButtonRequestType',
  full_name='ButtonRequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_Other', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_FeeOverThreshold', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_ConfirmOutput', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_ResetDevice', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_ConfirmWord', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_WipeDevice', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_ProtectCall', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ButtonRequest_SignTx', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1180,
  serialized_end=1442,
)

ButtonRequestType = enum_type_wrapper.EnumTypeWrapper(_BUTTONREQUESTTYPE)
Failure_UnexpectedMessage = 1
Failure_ButtonExpected = 2
Failure_SyntaxError = 3
Failure_ActionCancelled = 4
Failure_PinExpected = 5
Failure_PinCancelled = 6
Failure_PinInvalid = 7
Failure_InvalidSignature = 8
Failure_Other = 9
Failure_NotEnoughFunds = 10
Failure_NotInitialized = 11
Failure_FirmwareError = 99
PAYTOADDRESS = 0
PAYTOSCRIPTHASH = 1
TXINPUT = 0
TXOUTPUT = 1
ButtonRequest_Other = 1
ButtonRequest_FeeOverThreshold = 2
ButtonRequest_ConfirmOutput = 3
ButtonRequest_ResetDevice = 4
ButtonRequest_ConfirmWord = 5
ButtonRequest_WipeDevice = 6
ButtonRequest_ProtectCall = 7
ButtonRequest_SignTx = 8

BINARY_FIELD_NUMBER = 50001
binary = _descriptor.FieldDescriptor(
  name='binary', full_name='binary', index=0,
  number=50001, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
WIRE_IN_FIELD_NUMBER = 50002
wire_in = _descriptor.FieldDescriptor(
  name='wire_in', full_name='wire_in', index=1,
  number=50002, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
WIRE_OUT_FIELD_NUMBER = 50003
wire_out = _descriptor.FieldDescriptor(
  name='wire_out', full_name='wire_out', index=2,
  number=50003, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
WIRE_DEBUG_IN_FIELD_NUMBER = 50004
wire_debug_in = _descriptor.FieldDescriptor(
  name='wire_debug_in', full_name='wire_debug_in', index=3,
  number=50004, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
WIRE_DEBUG_OUT_FIELD_NUMBER = 50005
wire_debug_out = _descriptor.FieldDescriptor(
  name='wire_debug_out', full_name='wire_debug_out', index=4,
  number=50005, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_HDNODETYPE = _descriptor.Descriptor(
  name='HDNodeType',
  full_name='HDNodeType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='depth', full_name='HDNodeType.depth', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='HDNodeType.fingerprint', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='child_num', full_name='HDNodeType.child_num', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chain_code', full_name='HDNodeType.chain_code', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
    _descriptor.FieldDescriptor(
      name='private_key', full_name='HDNodeType.private_key', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='HDNodeType.public_key', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=50,
  serialized_end=196,
)


_COINTYPE = _descriptor.Descriptor(
  name='CoinType',
  full_name='CoinType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin_name', full_name='CoinType.coin_name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coin_shortcut', full_name='CoinType.coin_shortcut', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_type', full_name='CoinType.address_type', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxfee_kb', full_name='CoinType.maxfee_kb', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  extension_ranges=[],
  serialized_start=198,
  serialized_end=291,
)


_TXINPUTTYPE = _descriptor.Descriptor(
  name='TxInputType',
  full_name='TxInputType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_n', full_name='TxInputType.address_n', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_hash', full_name='TxInputType.prev_hash', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
    _descriptor.FieldDescriptor(
      name='prev_index', full_name='TxInputType.prev_index', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_sig', full_name='TxInputType.script_sig', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='TxInputType.sequence', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4294967295,
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
  extension_ranges=[],
  serialized_start=294,
  serialized_end=427,
)


_TXOUTPUTTYPE = _descriptor.Descriptor(
  name='TxOutputType',
  full_name='TxOutputType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='TxOutputType.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_n', full_name='TxOutputType.address_n', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='TxOutputType.amount', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_type', full_name='TxOutputType.script_type', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_args', full_name='TxOutputType.script_args', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=429,
  serialized_end=556,
)


_TXOUTPUTBINTYPE = _descriptor.Descriptor(
  name='TxOutputBinType',
  full_name='TxOutputBinType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='TxOutputBinType.amount', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_pubkey', full_name='TxOutputBinType.script_pubkey', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=558,
  serialized_end=620,
)


_TRANSACTIONTYPE = _descriptor.Descriptor(
  name='TransactionType',
  full_name='TransactionType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='TransactionType.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='TransactionType.inputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='TransactionType.outputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lock_time', full_name='TransactionType.lock_time', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  extension_ranges=[],
  serialized_start=622,
  serialized_end=746,
)

_TXOUTPUTTYPE.fields_by_name['script_type'].enum_type = _SCRIPTTYPE
_TRANSACTIONTYPE.fields_by_name['inputs'].message_type = _TXINPUTTYPE
_TRANSACTIONTYPE.fields_by_name['outputs'].message_type = _TXOUTPUTBINTYPE
DESCRIPTOR.message_types_by_name['HDNodeType'] = _HDNODETYPE
DESCRIPTOR.message_types_by_name['CoinType'] = _COINTYPE
DESCRIPTOR.message_types_by_name['TxInputType'] = _TXINPUTTYPE
DESCRIPTOR.message_types_by_name['TxOutputType'] = _TXOUTPUTTYPE
DESCRIPTOR.message_types_by_name['TxOutputBinType'] = _TXOUTPUTBINTYPE
DESCRIPTOR.message_types_by_name['TransactionType'] = _TRANSACTIONTYPE

class HDNodeType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HDNODETYPE

  # @@protoc_insertion_point(class_scope:HDNodeType)

class CoinType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COINTYPE

  # @@protoc_insertion_point(class_scope:CoinType)

class TxInputType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXINPUTTYPE

  # @@protoc_insertion_point(class_scope:TxInputType)

class TxOutputType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXOUTPUTTYPE

  # @@protoc_insertion_point(class_scope:TxOutputType)

class TxOutputBinType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXOUTPUTBINTYPE

  # @@protoc_insertion_point(class_scope:TxOutputBinType)

class TransactionType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSACTIONTYPE

  # @@protoc_insertion_point(class_scope:TransactionType)

google.protobuf.descriptor_pb2.FieldOptions.RegisterExtension(binary)
google.protobuf.descriptor_pb2.EnumValueOptions.RegisterExtension(wire_in)
google.protobuf.descriptor_pb2.EnumValueOptions.RegisterExtension(wire_out)
google.protobuf.descriptor_pb2.EnumValueOptions.RegisterExtension(wire_debug_in)
google.protobuf.descriptor_pb2.EnumValueOptions.RegisterExtension(wire_debug_out)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n(org.multibit.hd.hardware.trezor.protobufB\nTrezorType')
_HDNODETYPE.fields_by_name['chain_code'].has_options = True
_HDNODETYPE.fields_by_name['chain_code']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_HDNODETYPE.fields_by_name['private_key'].has_options = True
_HDNODETYPE.fields_by_name['private_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_HDNODETYPE.fields_by_name['public_key'].has_options = True
_HDNODETYPE.fields_by_name['public_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_TXINPUTTYPE.fields_by_name['prev_hash'].has_options = True
_TXINPUTTYPE.fields_by_name['prev_hash']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_TXINPUTTYPE.fields_by_name['script_sig'].has_options = True
_TXINPUTTYPE.fields_by_name['script_sig']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_TXOUTPUTTYPE.fields_by_name['script_args'].has_options = True
_TXOUTPUTTYPE.fields_by_name['script_args']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
_TXOUTPUTBINTYPE.fields_by_name['script_pubkey'].has_options = True
_TXOUTPUTBINTYPE.fields_by_name['script_pubkey']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\210\265\030\001')
# @@protoc_insertion_point(module_scope)
