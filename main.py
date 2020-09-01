# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from collections import OrderedDict

def decode(self, filename):
    with open(filename, 'rb') as f:
        meta_info = f.read()
    if not isinstance(meta_info, bytes):
        raise TypeError('Argument "data" must be of type bytes')
    self._data = meta_info
    self._index = 0
    c = self._data[self._index:self._index + 1]

    if c == b'd':
        self._index += 1
        colon = self._data[self._index:self._index+1]
        next_index = int(colon)
        print(next_index)
        self._index = self._data.index(b':', self._index)
        print(self._index)
        self._index += 1
        print(self._data[self._index:self._index + next_index])
        c = self._data[self._index + next_index:self._index + next_index+1]
        self._index+=next_index
    if c in b'0123456789':
        _length = self._data.index(b':', self._index)
        next_index = self._data[self._index:_length]
        print(next_index)

def _read_until(self, separated:bytes):
    self.

def _read_str(self, length:int):



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(decode('hunt.torrent'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
