# Documentation about this PoC is here: http://www.vallejo.cc/2019/05/poc-encrypting-malicious-script-into.html
# Author: Javier Vicente Vallejo
# Tool to encode a given content into unicode invisible characters

import binascii
import sys

try:
    f = open(sys.argv[1])
    s = f.read()
    f.close()
except:
    s = "import os\r\nos.system(\"c:\\windows\\system32\\calc.exe\")"
    print "error, encoding default script", s

#online string -> bits  and   bits -> string from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa

s2 = ''.join(map(lambda x: ["\xe2\x80\x8b", "\xe2\x80\x8c"][x], map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in s]))))

print binascii.hexlify(s2)

s3 = "".join(chr(int("".join(map(str,s2.replace("\xe2\x80\x8b", "0").replace("\xe2\x80\x8c", "1")[i:i+8])),2)) for i in range(0,len(map(int, s2.replace("\xe2\x80\x8b", "0").replace("\xe2\x80\x8c", "1"))),8))

print s3