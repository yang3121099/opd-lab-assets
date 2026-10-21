import sys
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

def process_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    output = []
    for idx, line in enumerate(lines):
        line = line.rstrip('\n')
        transformed = transform(line)
        encoded = encode_block(transformed)
        output.append(f"Line {idx+1}: {encoded}")
    return output

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: mystery.py <input_file>")
        sys.exit(1)
    results = process_file(sys.argv[1])
    for r in results:
        print(r)
