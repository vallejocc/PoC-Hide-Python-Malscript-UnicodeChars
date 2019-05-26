s = '''‍​‌‌​‌​​‌​‌‌​‌‌​‌​‌‌‌​​​​​‌‌​‌‌‌‌​‌‌‌​​‌​​‌‌‌​‌​​​​‌​​​​​​‌‌​‌‌‌‌​‌‌‌​​‌‌​​​​‌‌​‌​​​​‌​‌​​‌‌​‌‌‌‌​‌‌‌​​‌‌​​‌​‌‌‌​​‌‌‌​​‌‌​‌‌‌‌​​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​‌​‌​‌‌​‌‌​‌​​‌​‌​​​​​‌​​​‌​​‌‌​​​‌‌​​‌‌‌​‌​​‌​‌‌‌​​​‌‌‌​‌‌‌​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌​​‌​​​‌‌​‌‌‌‌​‌‌‌​‌‌‌​‌‌‌​​‌‌​‌​‌‌‌​​​‌‌‌​​‌‌​‌‌‌‌​​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​​‌​‌​‌‌​‌‌​‌​​‌‌​​‌‌​​‌‌​​‌​​‌​‌‌‌​​​‌‌​​​‌‌​‌‌​​​​‌​‌‌​‌‌​​​‌‌​​​‌‌​​‌​‌‌‌​​‌‌​​‌​‌​‌‌‌‌​​​​‌‌​​‌​‌​​‌​​​‌​​​‌​‌​​‌‍Hello World'''
#decrypt the encoded "malicious" code 
#remove unicode bytes
s = s.split("\xe2\x80\x8d")[1].replace("\xe2\x80","")
#0x8b = bit 0   0x8c = bit 1
l = map(lambda x: x-0x8b, map(ord, s))
#bits -> string (from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa)
exec("".join(chr(int("".join(map(str,l[i:i+8])),2)) for i in range(0,len(l),8)))

#oneline
#exec("".join(chr(int("".join(map(str, s.split("\xe2\x80\x8d")[1].replace("\xe2\x80\x8b", "0").replace("\xe2\x80\x8c", "1")[i:i+8])),2)) for i in range(0,len(map(int, s.split("\xe2\x80\x8d")[1].replace("\xe2\x80\x8b", "0").replace("\xe2\x80\x8c", "1"))),8)))