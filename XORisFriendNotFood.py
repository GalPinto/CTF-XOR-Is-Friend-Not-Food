cipher = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'
print(" cipher:\t",end=" ")
for a in cipher:
    print(a,end=" ") # print cipher in decimal

def binary(n): # this function converts decimal to organized binary byte
    return "{0:{fill}8b}".format(n, fill='0')

decoded = ""
x = [106,111,119,108,115,106,111,119,108,115,106,111,119,108,115,106,111,119,108,115,106,111,119,108,115] # xor keys
# had to xor first and last bytes to get ctflearn{...} using the hint from the ctf
# u can notice the sequence so fill in the gaps and get the flag at the full xor execution

print("\n xors:\t\t",end=" ")
for a in x:
    print(a,end=" ") # print xor key list
print("\n decimal:\t",end=" ")
for i in range(len(x)):
    print(cipher[i]^x[i],end=" ") # print decryption in decimal
for i in range(len(x)):
    decoded = decoded + chr(cipher[i]^x[i])
print("\n decoded:\t",decoded)  # print decoded text