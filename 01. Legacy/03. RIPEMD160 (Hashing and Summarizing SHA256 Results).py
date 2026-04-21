# EIPEMD160 (RACE INTEGRITY PRIMITIVE EVALUATION MESSAGE DIGEST 160 BIT)
# SIMULASI HASHING PUBLIC KEY 
# JANGAN PERNAH KIRIM BITCOIN DARI ADDRESS UTAMA ANDA KE ADDRESS EKSPERIMENTAL INI KALAU MAU SIMULASI KIRIM DI HASIL AKHIR!!!
# JANGAN PERNAH PAKAI PRIVATE KEY INI DI WALLET ANDA!!! KARENA SUDAH TERSEBAR DI INTERNET
# MOHON BIJAK. INI HANYA EDUKASI SEMATA

# === RIPEMD160 (PURE, NO LIB) ===

def rol(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xffffffff              ### rotate left 32-bit


def f(j, x, y, z):
    ### fungsi nonlinear (berubah tiap ronde)
    if 0 <= j <= 15: return x ^ y ^ z
    if 16 <= j <= 31: return (x & y) | (~x & z)
    if 32 <= j <= 47: return (x | ~y) ^ z
    if 48 <= j <= 63: return (x & z) | (y & ~z)
    if 64 <= j <= 79: return x ^ (y | ~z)


# === CONSTANT (FIXED, JANGAN DIGANTI) ===
K  = [0x00000000,0x5A827999,0x6ED9EBA1,0x8F1BBCDC,0xA953FD4E]
KK = [0x50A28BE6,0x5C4DD124,0x6D703EF3,0x7A6D76E9,0x00000000]

r  = [
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
7,4,13,1,10,6,15,3,12,0,9,5,2,14,11,8,
3,10,14,4,9,15,8,1,2,7,0,6,13,11,5,12,
1,9,11,10,0,8,12,4,13,3,7,15,14,5,6,2,
4,0,5,9,7,12,2,10,14,1,3,8,11,6,15,13]

rr = [
5,14,7,0,9,2,11,4,13,6,15,8,1,10,3,12,
6,11,3,7,0,13,5,10,14,15,8,12,4,9,1,2,
15,5,1,3,7,14,6,9,11,8,12,2,10,0,4,13,
8,6,4,1,3,11,15,0,5,12,2,13,9,7,10,14,
12,15,10,4,1,5,8,7,6,2,13,14,0,3,9,11]

s  = [
11,14,15,12,5,8,7,9,11,13,14,15,6,7,9,8,
7,6,8,13,11,9,7,15,7,12,15,9,11,7,13,12,
11,13,6,7,14,9,13,15,14,8,13,6,5,12,7,5,
11,12,14,15,14,15,9,8,9,14,5,6,8,6,5,12,
9,15,5,11,6,8,13,12,5,12,13,14,11,8,5,6]

ss = [
8,9,9,11,13,15,15,5,7,7,8,11,14,14,12,6,
9,13,15,7,12,8,9,11,7,7,12,7,6,15,13,11,
9,7,15,11,8,6,6,14,12,13,5,14,13,13,7,5,
15,5,8,11,14,14,6,14,6,9,12,9,12,5,15,8,
8,5,12,9,12,5,14,6,8,13,6,5,15,13,11,11]


def ripemd160(msg):
    ### ===== VALIDASI INPUT =====
    if not isinstance(msg, bytes):
        raise TypeError("Input harus bytes")

    ### ===== PADDING =====
    length = len(msg) * 8
    msg += b'\x80'

    while (len(msg) * 8) % 512 != 448:
        msg += b'\x00'

    msg += length.to_bytes(8, 'little')                          ### RIPEMD pakai little-endian


    ### ===== INITIAL STATE =====
    h0,h1,h2,h3,h4 = 0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0


    ### ===== PROCESS =====
    for i in range(0, len(msg), 64):

        X = [int.from_bytes(msg[i+j:i+j+4], 'little') for j in range(0,64,4)]

        A,B,C,D,E = h0,h1,h2,h3,h4
        AA,BB,CC,DD,EE = h0,h1,h2,h3,h4

        for j in range(80):

            ### left line
            T = (rol((A + f(j,B,C,D) + X[r[j]] + K[j//16]) & 0xffffffff, s[j]) + E) & 0xffffffff
            A,E,D,C,B = E,D,rol(C,10),B,T

            ### right line (reverse logic)
            T = (rol((AA + f(79-j,BB,CC,DD) + X[rr[j]] + KK[j//16]) & 0xffffffff, ss[j]) + EE) & 0xffffffff
            AA,EE,DD,CC,BB = EE,DD,rol(CC,10),BB,T


        ### combine hasil
        T = (h1 + C + DD) & 0xffffffff
        h1 = (h2 + D + EE) & 0xffffffff
        h2 = (h3 + E + AA) & 0xffffffff
        h3 = (h4 + A + BB) & 0xffffffff
        h4 = (h0 + B + CC) & 0xffffffff
        h0 = T


    ### ===== OUTPUT =====
    return ''.join(x.to_bytes(4,'little').hex() for x in [h0,h1,h2,h3,h4])


# === MAIN ===
if __name__ == "__main__":

    
    sha_hex = "37d0987b72de5687eda73760e45611c8defc940b12a8feffdde08c5dbd429705"   ## <--------- Masukkan hasil SHA256 (hex) disini

    msg = bytes.fromhex(sha_hex)                                  ### convert ke bytes

    result = ripemd160(msg)

    print("HASIL RIPEMD160:")
    print(result)
