########################################################################
#
#       Author:  The Blosc development team - blosc@blosc.org
#
########################################################################


import array

# Compress and decompress different arrays
import blosc2

a = array.array("i", range(1000 * 1000))
a_bytesobj = a.tobytes()
c_bytesobj = blosc2.compress(a_bytesobj, typesize=4)
assert len(c_bytesobj) < len(a_bytesobj)
a_bytesobj2 = blosc2.decompress(c_bytesobj)
assert a_bytesobj == a_bytesobj2

dest = blosc2.compress(b"", 1)
assert b"" == blosc2.decompress(dest)
assert type(blosc2.decompress(blosc2.compress(b"1" * 7, 1), as_bytearray=True)) is bytearray
