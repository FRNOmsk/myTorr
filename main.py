# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from collections import OrderedDict

def decode(filename):
    with open(filename, 'rb') as f:
        meta_info = f.read()
        # meta_info = bencoding.Decoder(meta_info).decode()
    # retunr meta_info

    if not isinstance(meta_info, bytes):
        raise TypeError('Argument "data" must be of type bytes')
    _data = meta_info
    _index = 0

    if _index + 1 >= len(_data):
        return None
    c = _data[_index:_index + 1]
    # return c

    if c == b'd':
        _index += 1
        colon = _data[_index:_index+1]
        next_index = int(colon)
        print(next_index)
        _index = _data.index(b':', _index)
        print(_index)
        _index += 1
        print(_data[_index:_index + next_index])

        
    #     res = OrderedDict()
    #     while _data[_index: _index + 1] != b'e':
    #         _index += 1
    #         print(_data[_index:_index+1])

    # while _data[_index:_index + 1] != b'e':
    #     res = []
    #     res.append(_data[])
    #     _index += 1

    # return res



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(decode('hunt.torrent'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
