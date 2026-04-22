# Konversi Taproot Output Key -> Bech32m Address
# witness version = 1
# HRP = bc


# GANTI dengan Qx hasil code sebelumnya
prog_hex = "28bac758f70d663d786ed682325a81bf56fc0cc7963f58b328cc61aec1949d06"


# Bech32 charset

CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"  # Udah standar Pieter Wuille dan Gregory Maxwell


# polymod

def polymod(values):
    GEN = [0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3]
    chk = 1

    for v in values:
        top = chk >> 25
        chk = ((chk & 0x1ffffff) << 5) ^ v

        for i in range(5):
            if ((top >> i) & 1):
                chk ^= GEN[i]

    return chk

# hrp expand

def hrp_expand(hrp):
    out = []

    for c in hrp:
        out.append(ord(c) >> 5)

    out.append(0)

    for c in hrp:
        out.append(ord(c) & 31)

    return out


# create checksum (Bech32m)

def create_checksum(hrp, data):
    const = 0x2bc830a3   # Bech32m constant
    values = hrp_expand(hrp) + data + [0,0,0,0,0,0]

    pm = polymod(values) ^ const

    ret = []
    for i in range(6):
        ret.append((pm >> (5*(5-i))) & 31)

    return ret


# convert bits 8 -> 5

def convertbits(data, frombits, tobits, pad=True):
    acc = 0
    bits = 0
    ret = []
    maxv = (1 << tobits) - 1

    for value in data:
        acc = (acc << frombits) | value
        bits += frombits

        while bits >= tobits:
            bits -= tobits
            ret.append((acc >> bits) & maxv)

    if pad:
        if bits:
            ret.append((acc << (tobits - bits)) & maxv)

    return ret


# encode

def bech32m_encode(hrp, witver, prog):
    data = [witver] + convertbits(prog, 8, 5, True)
    checksum = create_checksum(hrp, data)
    combined = data + checksum

    return hrp + "1" + "".join(CHARSET[d] for d in combined)


# MAIN

program = bytes.fromhex(prog_hex)

addr = bech32m_encode("bc", 1, program)

print("Taproot Address:")
print(addr)
