#!/usr/bin/env python
# coding: utf-8

# In[233]:


#!/usr/bin/env python


# In[153]:


def SHR(x, n):
    '''FIPS PUB 180-4 section 3.2
    bit-wise right shift n times'''
    S = x >> n
    return S & 0xFFFFFFFFFFFFFFFF

def ROTR(x, n):
    '''FIPS PUB 180-4 section 3.2
    circular bit-wise right shift n times'''
    return ((x >> n) | (x << (64-n))) & 0xFFFFFFFFFFFFFFFF

def Ch(x, y, z):
    '''FIPS PUB 180-4 section 4.1.3 (4.8)
    a function used by SHA512/256'''
    return ((x & y)^((~x) & z)) & 0xFFFFFFFFFFFFFFFF

def Maj(x, y, z):
    '''FIPS PUB 180-4 section 4.1.3 (4.9)
    a function used by SHA512/256'''
    return ((x & y)^(x & z)^(y & z)) & 0xFFFFFFFFFFFFFFFF

def S_0_512(x):
    '''FIPS PUB 180-4 section 4.1.3 (4.10)
    a function used by SHA512/256'''
    return (ROTR(x, 28)^ROTR(x, 34)^ROTR(x, 39)) & 0xFFFFFFFFFFFFFFFF

def S_1_512(x):
    '''FIPS PUB 180-4 section 4.1.3 (4.11)
    a function used by SHA512/256'''
    return (ROTR(x, 14)^ROTR(x, 18)^ROTR(x, 41)) & 0xFFFFFFFFFFFFFFFF

def D_0_512(x):
    '''FIPS PUB 180-4 section 4.1.3 (4.12)
    a function used by SHA512/256'''
    return (ROTR(x, 1)^ROTR(x, 8)^SHR(x, 7)) & 0xFFFFFFFFFFFFFFFF

def D_1_512(x):
    '''FIPS PUB 180-4 section 4.1.3 (4.13)
    a function used by SHA512/256'''
    return (ROTR(x, 19)^ROTR(x, 61)^SHR(x, 6)) & 0xFFFFFFFFFFFFFFFF




# In[110]:

'''FIPS PUB 180-4 section 4.2.3
    80 64-bit constants used for schedule generation in SHA512/256
    these constants represent the first 64 bits of the fractional parts of cubic roots of the first 80 prime numbers'''
K = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
          0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
          0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
          0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
          0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
          0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
          0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
          0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
          0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
          0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
          0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
          0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
          0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
          0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
          0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
          0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
          0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
          0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
          0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
          0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817]

'''FIPS PUB 180-4 section 5.3.6.2
    the initial hash values used by SHA512/256'''
H = [0x22312194FC2BF72C, 0x9F555FA3C84C64C2, 0x2393B86B6F53B151, 0x963877195940EABD,
          0x96283EE2A88EFFE3, 0xBE5E1E2553863992, 0x2B0199FC2C85B8AA, 0x0EB72DDC81C52CA2]


# In[1]:



# In[2]:

'''RFC 8017 section 4.1
    used to convert an integer value x into an octet string of length xLen'''
def I2OSP(x, xLen):
    xL = x
    if x>= (256**xLen):
        return "integer too large"
    s = ''
    for i in range(xLen):
        s += chr(xL % 256)
        xL = xL // 256
    return s

'''RFC 8017 section 4.2
    used to convert an octet string s into an integer value'''
def OS2IP(s):
    xLen = len(s)
    x = 0
    for i in range(xLen):
        x += ord(s[i])*(256**(xLen-i-1))
    return x

'''utility function created to avoid code repetition
    takes an integer value n and returns the minimal amount of bytes needed to represent it'''
def nLen(n):
    k = 0
    while (n!=0):
        k+=1
        n>>=8
    return k

# In[151]:

'''FIPS PUB 180-4 section 5.1.2
    a padding function which appends a message M so that it's bit length is a multiple of 1024'''
def pad(M):
    l = M.bit_length()
    if (l % 8 != 0):
        l += ((-1*l) % 8)
    k = 0
    while ((l+1+k) % 1024 != 896):
        k+=1
    M = (M << 1) + 1
    M = (M << k)
    M = (M << 128) + l
    return M



'''FIPS PUB 180-4 section 6.4.2, 6.7
    the algorithm for calculating the 256-bit truncate of a 512-bit hash of message M'''
def SHA_512_256(M):
    M = OS2IP(M)
    M = pad(M)
    #print(hex(M))
    mA = []
    Ha = [H]
    while (M>0):
        mA.append(M % (2**1024))
        M = M // (2**1024)
    N = len(mA)
    mA.reverse()
    for i in range(1, N+1):
        W = [0 for i in range(80)]
        for t in range(16):
            W[15-t] = (mA[i-1] % (2**64)) & 0xFFFFFFFFFFFFFFFF
            mA[i-1] = mA[i-1] >> 64
        for t in range(16, 80):
            W[t] = (D_1_512(W[t-2])+W[t-7]+D_0_512(W[t-15])+W[t-16]) & 0xFFFFFFFFFFFFFFFF
        a, b, c, d, e, f, g, h = Ha[i-1]
        for t in range(80):
            T_1 = ((h + S_1_512(e) + Ch(e, f, g) + K[t] + W[t])) & 0xFFFFFFFFFFFFFFFF
            T_2 = (S_0_512(a) + Maj(a, b, c)) & 0xFFFFFFFFFFFFFFFF
            #h, g, f, e, d, c, b, a = g, f, e, (d + T_1) & 0xFFFFFFFFFFFFFFFF, c, b, a, (T_1 + T_2) & 0xFFFFFFFFFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + T_1) & 0xFFFFFFFFFFFFFFFF
            d = c
            c = b
            b = a
            a = (T_1 + T_2) & 0xFFFFFFFFFFFFFFFF
        H0 = (a + Ha[i-1][0]) % (2**64)  
        H1 = (b + Ha[i-1][1]) % (2**64)  
        H2 = (c + Ha[i-1][2]) % (2**64)  
        H3 = (d + Ha[i-1][3]) % (2**64)  
        H4 = (e + Ha[i-1][4]) % (2**64)  
        H5 = (f + Ha[i-1][5]) % (2**64)  
        H6 = (g + Ha[i-1][6]) % (2**64)  
        H7 = (h + Ha[i-1][7]) % (2**64)
        Ha.append([H0, H1, H2, H3, H4, H5, H6, H7])        
    Hash =  Ha[N][0]*(2**(64*3)) + Ha[N][1]*(2**(64*2)) + Ha[N][2]*(2**64) + Ha[N][3]
    return(Hash)
        

# In[55]:


'''RFC 8017 section 5.2.1
    generates a signature representative using a private key (n, d) of message representative m'''
def RSASP1(n, d , m):
    if m <0 or m>n -1:
        return "message representative out of range"
    else :
        return pow(m, d, n)


# In[3]:


'''RFC 8017 section 5.2.2
    calcilates message representative m using public key (n, e) of signatrue representative s'''
def RSAVP1(n, e, s):
    if s <0 or s> n -1:
        return "signature representative out of range"
    else :
        return pow(s, e, n)


# In[87]:


'''RFC 8017 section 9.2
    encodes a message using EMSA-PKCS1 encoding
    this function was modified to only work with SHA512/256 hash types'''
def EMSA_PKCS1_v1_5_ENCODE(M, emLen):
    H = (SHA_512_256(M))
    if H == "message too long":
        return "message too long"
    T = ("0x3031300d060960864801650304020605000420" + hex(H)[2:])
    tLen = len(T)
    if emLen < tLen + 11:
        return "intended encoded message length too short"
    PS = chr(0xff)*(emLen - tLen - 3)
    EM = chr(0x00) + chr(0x01) + PS + "00" + T
    return EM


# In[244]:


'''RFC 8017 section 8.2.1
    generates a signature of message M using private key (n, d)'''
def RSASSA_PKCS1_V1_5_SIGN(n, d, M):
    k = nLen(n)
    EM = EMSA_PKCS1_v1_5_ENCODE(M, k)
    m = OS2IP(EM)
    s = RSASP1(n, d, m)
    if s == "message representative out of range":
        return s
    S = I2OSP(s, k)
    return S


# In[241]:


'''RFC 8017 section 8.2.2
    verifies a signature s against a message M using the public key (n, e)'''
def RSASSA_PKCS1_V1_5_VERIFY(n, e, M, S):
    s = OS2IP(S)
    k = nLen(n)
    if nLen(s) != k:
        return "invalid signature"
    m = RSAVP1 (n, e, s)
    if m == "signature representative out of range":
        return "invalid signature"
    EM = I2OSP (m, k)
    if EM == "integer too large":
        return "invalid signature"
    EM1 = EMSA_PKCS1_v1_5_ENCODE(M, k)
    if EM1 == "message too long":
        return "message too long"
    if EM1 == "intended encoded message length too short":
        return "RSA modulus too short"
    if EM == EM1:
        return "valid signature"
    return "invalid signature"


# In[ ]:





# In[ ]:




