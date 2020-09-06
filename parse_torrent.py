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
            next_index = int(self._read_until(b':'))
            print(self._data[self._index:self._index + next_index])
            self._return(next_index)
            # c = self._data[self._index + next_index:self._index + next_index + 1]
            self._index += next_index
            c = self.next_c()
        if c in b'0123456789':
            next_index = int(self._read_until(b':'))
            print(self._data[self._index:self._index + next_index])
            self._return(next_index)
            self._index += next_index
            self.decode()
        if c == b'l':
            self._index += 1
            res = []
            while self._data[self._index:self._index + 1] != b'e':
                res.append(self.decode())
            # print(len(res))
            self._index += 1


    def next_c(self):
        return self._data[self._index:self._index + 1]

    def _read_until(self, separated:bytes) -> bytes:
        occurrence = self._data.index(separated, self._index)
        result = self._data[self._index: occurrence]
        self._index = occurrence + 1
        return result
    def _return(self, next_index):
        return self._data[self._index:self._index + next_index]
    # def _read_str(self, length:int):

