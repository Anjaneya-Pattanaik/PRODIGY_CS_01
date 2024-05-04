print("Welcome to Caesar Cipher Coder!!!\nOptions:\n1. Encode\t2. Decode\t3. Exit")
def code(s,off):
    if off in (-26,0,26):
        return s
    if off<0:
        off+=26
    res=""
    for c in s:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            x = ord(c) - base
            nxt = (x + off) % 26
            res += chr(base + nxt)
        else:
            res += c
    return res
        
while (True):
    opt=int(input("Enter option: "))
    if opt==1:
        s=input("Enter code: ")
        off=int(input("Enter offset (>=-26 & <=26): "))
        print("Result = ",code(s,off))
    elif opt==2:
        s=input("Enter code: ")
        off=int(input("Enter offset (>=-26 & <=26): "))
        print("Result = ",code(s,-off))
    elif opt==3:
        print("Thankyou!!")
        break
    else:
        print("Invalid Option!")
