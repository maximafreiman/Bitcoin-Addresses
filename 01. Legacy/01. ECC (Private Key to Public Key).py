# ================================
# ECC: PRIVATE KEY → PUBLIC KEY
# (secp256k1, tanpa library)
# ================================

# ---------- PARAMETER KURVA ----------
# kurva: y^2 = x^3 + 7
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

# generator point (G)
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337460388
G = (Gx, Gy)

# ---------- MASUKKAN PRIVATE KEY DISINI!! ----------
priv_hex = "7f3a9c5e8b2d4f1a6c9e0b3d5a7f8c2e1d4b6a9f0c3e7b2a5d8f1c6e9a4b3c2d"
k = int(priv_hex, 16)

print("Private Key:")
print(priv_hex)

# ---------- RUMUS ECC ----------
def inv(n, p):
    return pow(n, -1, p)

def point_add(P, Q):
    if P is None: return Q
    if Q is None: return P
    
    x1, y1 = P
    x2, y2 = Q
    
    # titik invers → hasil infinity
    if x1 == x2 and y1 != y2:
        return None
    
    if P == Q:
        # point doubling
        m = (3 * x1 * x1) * inv(2 * y1, p) % p
    else:
        # point addition
        m = (y2 - y1) * inv(x2 - x1, p) % p
    
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    
    return (x3, y3)

def scalar_mult(k, P):
    result = None
    addend = P
    
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    
    return result

# ---------- HITUNG PUBLIC KEY ----------
pub = scalar_mult(k, G)

x, y = pub

print("\nPublic Key (X, Y):")
print("X =", format(x, '064x'))
print("Y =", format(y, '064x'))

# ---------- FORMAT BITCOIN ----------
# uncompressed
pub_uncompressed = "04" + format(x, '064x') + format(y, '064x')

# compressed
prefix = "02" if y % 2 == 0 else "03"
pub_compressed = prefix + format(x, '064x')

print("\nPublic Key (Uncompressed):")
print(pub_uncompressed)

print("\nPublic Key (Compressed):")
print(pub_compressed)
