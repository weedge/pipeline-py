# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_frames.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64\x61ta_frames.proto\x12\x0fpipeline_frames\"3\n\tTextFrame\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\"c\n\rAudioRawFrame\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x61udio\x18\x03 \x01(\x0c\x12\x13\n\x0bsample_rate\x18\x04 \x01(\r\x12\x14\n\x0cnum_channels\x18\x05 \x01(\r\"K\n\rImageRawFrame\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\r\x12\r\n\x05hight\x18\x03 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x04 \x01(\t\"\x9e\x01\n\x05\x46rame\x12*\n\x04text\x18\x01 \x01(\x0b\x32\x1a.pipeline_frames.TextFrameH\x00\x12/\n\x05\x61udio\x18\x02 \x01(\x0b\x32\x1e.pipeline_frames.AudioRawFrameH\x00\x12/\n\x05image\x18\x03 \x01(\x0b\x32\x1e.pipeline_frames.ImageRawFrameH\x00\x42\x07\n\x05\x66rameb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_frames_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TEXTFRAME']._serialized_start=38
  _globals['_TEXTFRAME']._serialized_end=89
  _globals['_AUDIORAWFRAME']._serialized_start=91
  _globals['_AUDIORAWFRAME']._serialized_end=190
  _globals['_IMAGERAWFRAME']._serialized_start=192
  _globals['_IMAGERAWFRAME']._serialized_end=267
  _globals['_FRAME']._serialized_start=270
  _globals['_FRAME']._serialized_end=428
# @@protoc_insertion_point(module_scope)
