import math
f = open('2015/Day 4/test.txt', 'r')

test = f.read()
secredKey = 'They are deterministic'

def F(x, y, z):
    return (int(x, 2) & int(y, 2)) | (int(Not(x), 2) & int(z, 2))

def G(x, y, z):
    return (int(x, 2) & int(z, 2)) | (int(y, 2) & int(Not(z), 2))

def H(x, y, z):
    return (int(x, 2) ^ int(y, 2) ^ int(z, 2))

def I(x, y, z):
    return (int(y, 2) ^ (int(x, 2) | int(Not(z), 2)))

def Not(x):
    if x.find('b') != -1:
        x= x[2:]
    x = x.replace('1', '.')
    x = x.replace('0', '1')
    x = x.replace('.', '0')
    return x


# Formating string to bits
message = ''.join(format(ord(i), '08b') for i in secredKey)

# Appending 1 bit
message += '1'

# Padding message with zeroes
temp = len(message)%512
if temp < 448:
    message += '0' * (448 - temp)
else:
    message += '0' * (512 - temp + 448)
    

# Appending last 448bit chunk with secredKey length in bits
temp = bin(len(secredKey)%pow(2, 64))
message += '0'*(64 - len(temp)+2) + temp[2:]

# Creating a list of constants Ks
K = [bin(math.floor(abs(math.sin(i+ 1))*pow(2, 32))) for i in range(0,64)]

# Creating a list of per-round shift amounts
S = []
S.extend([7, 12, 17, 22]*4)
S.extend([5,  9, 14, 20]*4)
S.extend([4, 11, 16, 23]*4)
S.extend([6, 10, 15, 21]*4)

# Initialization vectors
A_init = '00000001001000110100010101100111' # Hex 01234567
B_init = '10001001101010111100110111101111' # Hex 89abcdef
C_init = '11111110110111001011101010011000' # Hex fedcba98
D_init = '01110110010101000011001000010000' # Hex 76543210

Aa = A_init
Bb = B_init
Cc = C_init
Dd = D_init


for i in range(int(len(message)/512)):
    
    # Getting proper chunk from message
    chunk = message[i*512:(i+1)*512]
    
    # Creating list of "words"
    M = [chunk[x*32:(x+1)*32] for x in range(16)]
    
    g = 0
    for x in range(64):
        if g > 15:
            g = g%16
        # print(str(x) + ": " + str(g))
        
        if x < 16:
            temp = F(Bb, Cc, Dd)
            temp = (int(Aa, 2) + temp)%4294967296
            temp = (int(M[g], 2) + temp)%4294967296
            temp = (int(K[x], 2) + temp)%4294967296
            temp = bin(temp)[2:]
            temp = '0'*(len(temp)%4) + temp
            temp = int((temp[S[x]:] + temp[:S[x]]), 2)
            temp = (int(Bb, 2) + temp)%4294967296
            # print(hex(temp))
            temp = bin(temp)
            g += 1
            if x == 15:
                g = 1
                
        elif x < 32:
            temp = G(Bb, Cc, Dd)
            # print(hex(temp))
            temp = (int(Aa, 2) + temp)%4294967296
            temp = (int(M[g], 2) + temp)%4294967296
            temp = (int(K[x], 2) + temp)%4294967296
            temp = bin(temp)[2:]
            temp = '0'*(len(temp)%4) + temp
            temp = int((temp[S[x]:] + temp[:S[x]]), 2)
            temp = (int(Bb, 2) + temp)%4294967296
            temp = bin(temp)
            g += 5
            if x == 31:
                g = 5
                
        elif x < 48:
            temp = H(Bb, Cc, Dd)
            temp = (int(Aa, 2) + temp)%4294967296
            temp = (int(M[g], 2) + temp)%4294967296
            temp = (int(K[x], 2) + temp)%4294967296
            temp = bin(temp)[2:]
            temp = '0'*(len(temp)%4) + temp
            temp = int((temp[S[x]:] + temp[:S[x]]), 2)
            temp = (int(Bb, 2) + temp)%4294967296
            temp = bin(temp)
            g += 3
            if x == 47:
                g = 0
        else:
            temp = I(Bb, Cc, Dd)
            temp = (int(Aa, 2) + temp)%4294967296
            temp = (int(M[g], 2) + temp)%4294967296
            temp = (int(K[x], 2) + temp)%4294967296
            temp = bin(temp)[2:]
            temp = '0'*(len(temp)%4) + temp
            temp = int((temp[S[x]:] + temp[:S[x]]), 2)
            temp = (int(Bb, 2) + temp)%4294967296
            temp = bin(temp)
            g += 7
    
        A_temp = Aa
        B_temp = Bb
        C_temp = Cc
        D_temp = Dd
    
        Aa = D_temp
        Bb = temp
        Cc = B_temp
        Dd = C_temp
        print(hex(int(Aa,2)))
        print(hex(int(Bb,2)))
        print(hex(int(Cc,2)))
        print(hex(int(Dd,2)))
    
    A_init = bin((int(A_init, 2) + int(Aa, 2))%4294967296)
    B_init = bin((int(B_init, 2) + int(Bb, 2))%4294967296)
    C_init = bin((int(C_init, 2) + int(Cc, 2))%4294967296)
    D_init = bin((int(D_init, 2) + int(Dd, 2))%4294967296)
    
# print(A_init)
# print(B_init)
# print(C_init)
# print(D_init)

hash = hex(int(A_init, 2))[2:] + " " + hex(int(B_init, 2))[2:] + " " + hex(int(C_init, 2))[2:] + " " + hex(int(D_init, 2))[2:]
print(hash)

# First try - 234567 24def 168a98 21b250

# def G(x, y, z):
#     return (int(x, 2) & int(z, 2)) | (int(y, 2) & ~int(z, 2))

# 
# Testy
# 
# print(hex(G('101100001101001101111110100010', '11011110000101100111001110111110', '1001011100101110110001010000010')))
# temp = bin(735250928)[2:]
# temp = '0'*(len(temp)%4) + temp
# print(temp[:S[0]])
# print(int((temp[S[0]:] + temp[:S[0]]), 2))