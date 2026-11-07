# Decode the RAM

def decode_ram_utf8(data):
    contents = bytes.fromhex(data).decode("utf-8")
    return contents