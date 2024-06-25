import sys
import string

if len(sys.argv) != 2:
    print("Usage: python3 getFlag.py hex_encoded")
    sys.exit()

def ishex(s):
    try:
        n = int(s,16)
        return True
    except ValueError:
        return False

# hex_encoded="182c1d23277d053c3623091c24192338503333340d0a226b3620282930023e102968223e1c1f2a2a"
hex_encoded=sys.argv[1]

if not ishex(hex_encoded):
    print("Enter valid hex_encoded value")
    sys.exit()
elif len(hex_encoded)!=80:
    print("The hex_encoded length must be 80")
    sys.exit()

hex_encoded=bytes.fromhex(hex_encoded).decode()

flag_1_4="THM{"


key_1_4=""
for i in range(0,len(flag_1_4)):
    key_1_4 += chr(ord(hex_encoded[i]) ^ ord(flag_1_4[i]))

key_5=0
possible_chrs=0
flag=""

while possible_chrs<62:
    possible_last_key_chr = string.ascii_letters + string.digits
    key=key_1_4+possible_last_key_chr[key_5]
    for i in range(0,len(hex_encoded)):
        flag += chr(ord(hex_encoded[i]) ^ ord(key[i%len(key)]))

    flag = str(flag)
    try:
        if flag.endswith("}"):
            print(f"flag1 is {flag}")
            print(f"key is {key}")
            break
        else:
            flag=""
            key_5+=1
            possible_chrs+=1
    except:
        print('Something went wrong.')