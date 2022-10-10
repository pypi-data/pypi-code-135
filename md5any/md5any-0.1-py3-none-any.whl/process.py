import os

from .error import MD5AnyErrorCode
from .hash import hash

class Hash:
    def __init__(self, path):
        self._abs = self._hash_dir(path) if os.path.isdir(path) else self._hash_file(path)

    @property
    def absrtact(self):
        return self._abs

    @staticmethod
    def test(path):
        if not os.path.exists(path):
            errorMsg = "Invalid path {}".format(path)
            raise MD5AnyErrorCode(errorMsg)
        return path

    def _hash_file(self, filepath, dentry=None):
        if os.path.isdir(filepath):
            raise MD5AnyErrorCode("Not a regular file")

        try:
            with open(filepath, 'rb') as f:
                abs = hash(str(f.read()))
                if dentry is not None:
                    abs = hash(str(dentry) + str(abs))
                return abs
        except:
            raise MD5AnyErrorCode("Hash failed")

    def _hash_dir(self, dirpath, dentry=None):
        if not os.path.isdir(dirpath):
            raise MD5AnyErrorCode("Not a regular directory")

        hashList = []
        for root,dirs,files in os.walk(dirpath):
            for file in files:
                hashList.append(self._hash_file(os.path.join(root, file), dentry))
            for dir in dirs:
                hashList.append(self._hash_dir(os.path.join(root, dir), dir))
        hashList.sort()
        abs = hash(str(dentry) + ''.join(hashList))
        return abs
