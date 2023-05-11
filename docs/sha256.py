import sys
import hashlib

if len(sys.argv)!=2:
    print("args number error, use it like: > python sha256.py filename")
    exit()

data = open(sys.argv[1], "rb").read()
hsh  = hashlib.sha256(data).digest().hex().lower()

print(str(hsh))
