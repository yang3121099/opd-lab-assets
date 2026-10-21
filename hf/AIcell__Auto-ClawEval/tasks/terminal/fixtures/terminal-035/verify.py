import hashlib
import base64

def transform(data):
    result = []
    for i, ch in enumerate(data):
        shifted = (ord(ch) + i * 3) % 256
        result.append(shifted)
    return bytes(result)

def encode_block(block):
    h = hashlib.md5(block).hexdigest()[:8]
    b64 = base64.b64encode(block).decode('ascii')
    return f"{h}:{b64}"

lines = ["hello", "world", "foo"]
for idx, line in enumerate(lines):
    transformed = transform(line)
    encoded = encode_block(transformed)
    print(f"Line {idx+1}: {encoded}")
