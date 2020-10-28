from collections import OrderedDict

class Decode:
    def __init__(self,  data: bytes):
        # self._filename = filename
        # with open(self._filename, 'rb') as f:
        #     meta_info = f.read()
        if not isinstance(data, bytes):
            raise TypeError('Argument "data" must be of type bytes')
        self._data = data
        self._index = 0

    def decode(self):
            c = self.next_c()
            if c == b'i':
                self._index += 1
                return self._read_int()
            if c == b'd':
                self._index += 1
                return self._dict()
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
        return int(self._read_until(b'e'))

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

class Encoder:
    """
    Encodes a python object to a bencoded sequence of bytes.
    Supported python types is:
        - str
        - int
        - list
        - dict
        - bytes
    Any other type will simply be ignored.
    """
    def __init__(self, data):
        self._data = data

    def encode(self) -> bytes:
        """
        Encode a python object to a bencoded binary string
        :return The bencoded binary data
        """
        return self.encode_next(self._data)

    def encode_next(self, data):
        if type(data) == str:
            return self._encode_string(data)
        elif type(data) == int:
            return self._encode_int(data)
        elif type(data) == list:
            return self._encode_list(data)
        elif type(data) == dict or type(data) == OrderedDict:
            return self._encode_dict(data)
        elif type(data) == bytes:
            return self._encode_bytes(data)
        else:
            return None

    def _encode_int(self, value):
        return str.encode('i' + str(value) + 'e')

    def _encode_string(self, value: str):
        res = str(len(value)) + ':' + value
        return str.encode(res)

    def _encode_bytes(self, value: str):
        result = bytearray()
        result += str.encode(str(len(value)))
        result += b':'
        result += value
        return result

    def _encode_list(self, data):
        result = bytearray('l', 'utf-8')
        result += b''.join([self.encode_next(item) for item in data])
        result += b'e'
        return result

    def _encode_dict(self, data: dict) -> bytes:
        result = bytearray('d', 'utf-8')
        for k, v in data.items():
            key = self.encode_next(k)
            value = self.encode_next(v)
            if key and value:
                result += key
                result += value
            else:
                raise RuntimeError('Bad dict')
        result += b'e'
        return result