import struct
import binascii
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))