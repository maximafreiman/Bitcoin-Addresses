# === Curve Parameters (secp256k1) ===
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F   ### bilangan prima besar (semua operasi mod ini)
A = 0                                                                    ### parameter kurva (A = 0)
B = 7                                                                    ### parameter kurva (y^2 = x^3 + 7)

Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337460388
G = (Gx, Gy)                                                             ### titik generator (titik awal semua operasi)

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141   ### batas maksimum private key


# === Modular Inverse ===
def mod_inverse(k, p):
    ### fungsi untuk "membagi" dalam matematika modular
    if k == 0:
        raise ZeroDivisionError("division by zero")

    if k < 0:
        return p - mod_inverse(-k, p)

    s, old_s = 0, 1
    r, old_r = p, k

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s

    return old_s % p


# === Point Addition ===
def point_add(p1, p2):
    ### nambahin dua titik di kurva elliptic
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 and y1 != y2:
        return None                                                    ### hasilnya titik tak hingga

    if p1 == p2:
        m = (3 * x1 * x1 + A) * mod_inverse(2 * y1, P) % P            ### doubling
    else:
        m = (y2 - y1) * mod_inverse(x2 - x1, P) % P                   ### beda titik

    x3 = (m * m - x1 - x2) % P
    y3 = (m * (x1 - x3) - y1) % P

    return (x3, y3)


# === Scalar Multiplication ===
def scalar_mult(k, point):
    ### ini inti: private key × G
    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend)                        ### kalau bit = 1 → tambahin

        addend = point_add(addend, addend)                            ### doubling (lompat jauh)
        k >>= 1                                                       ### geser bit ke kanan

    return result


# === Generate Public Key ===
def generate_public_key(private_key):
    ### public key = private key × G
    return scalar_mult(private_key, G)


# === Compress Public Key ===
def compress_public_key(point):
    ### ubah (x, y) jadi format 33 byte (hemat)
    x, y = point
    prefix = 0x02 if y % 2 == 0 else 0x03                             ### genap = 02, ganjil = 03
    return bytes([prefix]) + x.to_bytes(32, 'big')


# === Decompress Public Key ===
def decompress_public_key(compressed_key):
    ### balikin compressed jadi (x, y)
    prefix = compressed_key[0]
    x = int.from_bytes(compressed_key[1:], 'big')

    y_squared = (x**3 + 7) % P                                        ### dari rumus kurva
    y = pow(y_squared, (P + 1) // 4, P)                               ### cari akar kuadrat modular

    if (y % 2 == 0 and prefix == 0x02) or (y % 2 == 1 and prefix == 0x03):
        return (x, y)
    else:
        return (x, P - y)


# === MAIN ===
if __name__ == "__main__":

    
    priv_hex = "7f3a9c5e8b2d4f1a6c9e0b3d5a7f8c2e1d4b6a9f0c3e7b2a5d8f1c6e9a4b3c2d"     # <----------------- Masukkan data (private key hex) disini

    private_key = int(priv_hex, 16)                                   ### convert string hex → integer

    public_key = generate_public_key(private_key)

    x, y = public_key

    print("=== PUBLIC KEY ===")
    print("X =", format(x, '064x'))                                   ### tampil hex 64 digit
    print("Y =", format(y, '064x'))

    compressed = compress_public_key(public_key)
    print("\n=== COMPRESSED ===")
    print(compressed.hex())

    decompressed = decompress_public_key(compressed)
    print("\n=== DECOMPRESSED ===")
    print("X =", format(decompressed[0], '064x'))
    print("Y =", format(decompressed[1], '064x'))
