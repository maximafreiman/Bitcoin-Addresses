


pubkey_hex = "033c83b7dff41e28512b667197db412a733767eaeeb2de4f56cc432bba027e7bc1"      ## <------------ Masukkan public key compressed (02/03 + 64 hex) Disini!



def hex_to_bytes(h):                                                                   # Mengubah hex string jadi bytes
    return bytes(int(h[i:i+2], 16) for i in range(0, len(h), 2))

pubkey_bytes = hex_to_bytes(pubkey_hex)



x_only = pubkey_bytes[1:]                                                              # Buang prefix 02/03 dari pubkey


K = [                                                                                  # Rumus SHA256 (JANGAN DIGANTI2!)
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    

] + [0]*48  

def rotr(x,n): return ((x>>n)|(x<<(32-n))) & 0xffffffff

def sha256(msg):
    msg = bytearray(msg)
    l = len(msg)*8

    msg.append(0x80)
    while (len(msg)+8)%64 != 0:
        msg.append(0)
    msg += l.to_bytes(8,'big')

    h = [
        0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
        0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
    ]

    for i in range(0,len(msg),64):
        w = [0]*64
        for t in range(16):
            w[t] = int.from_bytes(msg[i+t*4:i+t*4+4],'big')

        for t in range(16,64):
            s0 = rotr(w[t-15],7)^rotr(w[t-15],18)^(w[t-15]>>3)
            s1 = rotr(w[t-2],17)^rotr(w[t-2],19)^(w[t-2]>>10)
            w[t]=(w[t-16]+s0+w[t-7]+s1)&0xffffffff

        a,b,c,d,e,f,g,hv = h

        for t in range(64):
            S1 = rotr(e,6)^rotr(e,11)^rotr(e,25)
            ch = (e&f)^((~e)&g)
            temp1 = (hv + S1 + ch + K[t] + w[t]) & 0xffffffff
            S0 = rotr(a,2)^rotr(a,13)^rotr(a,22)
            maj = (a&b)^(a&c)^(b&c)
            temp2 = (S0 + maj) & 0xffffffff

            hv,g,f,e,d,c,b,a = g,f,e,(d+temp1)&0xffffffff,c,b,a,(temp1+temp2)&0xffffffff

        h = [(x+y)&0xffffffff for x,y in zip(h,[a,b,c,d,e,f,g,hv])]

    return b''.join(x.to_bytes(4,'big') for x in h)




tag = b"TapTweak"                                                                                   # PETUNJUK (Tagged Hash TapTweak) H("TapTweak", x_only)
tag_hash = sha256(tag)
tweak_bytes = sha256(tag_hash + tag_hash + x_only)
tweak_int = int.from_bytes(tweak_bytes,'big')




P  = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F                             # Parameter secp256k1 (Gx dan Gy udah paten berdasarkan kurva secp256k1)
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337460388





def modinv(a,p):                                                                                    # (Modular Inverse)
    return pow(a,p-2,p)




def point_add(x1,y1,x2,y2):                                                                         # (Point Addition)
    if x1==x2 and y1!=y2:
        return None

    if x1==x2:
        lam=(3*x1*x1)*modinv(2*y1,P)%P
    else:
        lam=(y2-y1)*modinv(x2-x1,P)%P

    x3=(lam*lam-x1-x2)%P
    y3=(lam*(x1-x3)-y1)%P
    return x3,y3



def scalar_mult(k,x,y):                                                                             # Scalar Multiplication
    r=None
    a=(x,y)
    while k:
        if k&1:
            r=a if r is None else point_add(r[0],r[1],a[0],a[1])
        a=point_add(a[0],a[1],a[0],a[1])
        k>>=1
    return r




x=int.from_bytes(x_only,'big')                                                                      # Decode Pubkey → (x,y)
y_sq=(x*x*x+7)%P
y=pow(y_sq,(P+1)//4,P)


if (pubkey_bytes[0]==3 and y%2==0) or (pubkey_bytes[0]==2 and y%2==1):                              #  Sesuaikan persamaan (02 genap, 03 ganjil)
    y=(-y)%P



tweak_point=scalar_mult(tweak_int,Gx,Gy)                                                            # PETUNJUK (Hitung tweak * G)

                                                   
Qx,Qy=point_add(x,y,tweak_point[0],tweak_point[1])                                                  # (Taproot Tweak)


                                                
output_key=Qx.to_bytes(32,'big')                                                                     # (OUTPUT KEY)

print("Output key:",output_key.hex())
