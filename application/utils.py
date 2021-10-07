import base64


def encode_value(value, encoding='ascii'):
    return base64.base64encode(str(value).encode(encoding)).decode(encoding)


def decode_value(value, encoding='ascii'):
    return base64.base64decode(str(value).encode(encoding)).decode(encoding)
