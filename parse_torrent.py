from collections import OrderedDict

class Decode:
    def __init__(self, filename):
        self._filename = filename
        with open(self._filename, 'rb') as f:
            meta_info = f.read()
        if not isinstance(meta_info, bytes):
            raise TypeError('Argument "data" must be of type bytes')
        self._data = meta_info
        self._index = 0

    def decode(self):
            c = self.next_c()
            if c == b'd':
                self._index += 1
                return self._dict()
            if c == b'i':
                self._index += 1
                return self._read_int()
            if c in b'0123456789':
                return self._read_str()
            if c == b'l':
                self._index += 1
                return self._list()


    def _list(self):
        resList = []
        while self._data[self._index:self._index + 1] != b'e':
            resList.append(self.decode())
        self._index += 1
        return resList

    def _read_int(self):
        return self._read_until(b'e')

    def next_c(self):
        return self._data[self._index:self._index + 1]

    def _dict(self):
        resDict = OrderedDict()
        while self._data[self._index: self._index + 1] != b'e':
            key = self.decode()
            obj = self.decode()
            resDict[key] = obj
        self._index += 1
        return resDict

    def _read_until(self, separated:bytes) -> bytes:
        occurrence = self._data.index(separated, self._index)
        result = self._data[self._index: occurrence]
        self._index = occurrence + 1
        return result

    def _read(self, length):
        res = self._data[self._index:self._index + length]
        self._index += length
        return res

    def _read_str(self):
        length = int(self._read_until(b':'))
        return self._read(length)

