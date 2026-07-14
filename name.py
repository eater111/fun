import hashlib

def make_handle(text, length=8):
    h = hashlib.sha256(text.encode()).hexdigest().upper()
    return "0x" + h[:length]

print(make_handle("纳祭库里波"))