# ==========================================
# RAW TAPROOT STEP 2 (NO LIBRARY)
# Compute Q = P + tweak*G
# Then output x(Q)
# ==========================================

# secp256k1 params
P_FIELD = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424

# ---------------------------
# modular inverse
# ---------------------------
def inv(a, n):
    return pow(a, n-2, n)

# ---------------------------
# point add
# ---------------------------
def point_add(A, B):
    if A is None:
        return B
    if B is None:
        return A

    x1,y1 = A
    x2,y2 = B

    if x1 == x2 and (y1 + y2) % P_FIELD == 0:
        return None

    if A != B:
        lam = ((y2 - y1) * inv(x2 - x1, P_FIELD)) % P_FIELD
    else:
        lam = ((3*x1*x1) * inv(2*y1, P_FIELD)) % P_FIELD

    x3 = (lam*lam - x1 - x2) % P_FIELD
    y3 = (lam*(x1 - x3) - y1) % P_FIELD

    return (x3,y3)

# ---------------------------
# scalar multiply
# ---------------------------
def scalar_mult(k, P):
    R = None
    addend = P

    while k > 0:
        if k & 1:
            R = point_add(R, addend)
        addend = point_add(addend, addend)
        k >>= 1

    return R

# ---------------------------
# decompress compressed pubkey
# ---------------------------
pubkey = "033c83b7dff41e28512b667197db412a733767eaeeb2de4f56cc432bba027e7bc1"

prefix = int(pubkey[:2],16)
x = int(pubkey[2:],16)

# y² = x³ + 7 mod p
y_sq = (pow(x,3,P_FIELD) + 7) % P_FIELD
y = pow(y_sq, (P_FIELD+1)//4, P_FIELD)

# choose parity
if y % 2 != (prefix % 2):
    y = P_FIELD - y

P = (x,y)

# ---------------------------
# tweak scalar (hasil sebelumnya)
# ---------------------------
tweak = int(
"0805a9f5b0c1b069a01caa2e274977980c85c47eab2b8de377ba732a1ddd78a4",
16
)

# ---------------------------
# Q = P + tweak*G
# ---------------------------
G = (Gx,Gy)

tG = scalar_mult(tweak, G)
Q = point_add(P, tG)

print("Qx =", hex(Q[0])[2:].zfill(64))
print("Qy =", hex(Q[1])[2:].zfill(64))
print("Taproot Output Key =", hex(Q[0])[2:].zfill(64))
