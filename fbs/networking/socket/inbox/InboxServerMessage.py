# automatically generated by the FlatBuffers compiler, do not modify

# namespace: inbox

import flatbuffers

class InboxServerMessage(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsInboxServerMessage(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InboxServerMessage()
        x.Init(buf, n + offset)
        return x

    # InboxServerMessage
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InboxServerMessage
    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # InboxServerMessage
    def Content(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def InboxServerMessageStart(builder): builder.StartObject(2)
def InboxServerMessageAddContentType(builder, contentType): builder.PrependUint8Slot(0, contentType, 0)
def InboxServerMessageAddContent(builder, content): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(content), 0)
def InboxServerMessageEnd(builder): return builder.EndObject()
