# CREATE BECH32 CHECKSUM


# Data With Witness Version
data = [
    0, 9, 29, 23, 6, 13, 7, 19, 5, 23, 24,
    11, 16, 29, 11, 16, 7, 27, 6, 19, 29,
    16, 7, 16, 24, 3, 10, 12, 8, 13, 31,
    22, 3
]

hrp = "bc"

# STEP 1: HRP EXPAND

def hrp_expand(text):
    left = []
    right = []

    for ch in text:
        code = ord(ch)
        left.append(code >> 5)
        right.append(code & 31)

    return left + [0] + right


# STEP 2: POLYMOD

def polymod(values):
    generators = [
        0x3b6a57b2,
        0x26508e6d,
        0x1ea119fa,
        0x3d4233dd,
        0x2a1462b3
    ]

    chk = 1

    for v in values:
        top = chk >> 25
        chk = ((chk & 0x1ffffff) << 5) ^ v

        for i in range(5):
            if (top >> i) & 1:
                chk ^= generators[i]

    return chk


# STEP 3: CREATE CHECKSUM

values = hrp_expand(hrp) + data + [0, 0, 0, 0, 0, 0]

pm = polymod(values) ^ 1

checksum = []

for i in range(6):
    value = (pm >> (5 * (5 - i))) & 31
    checksum.append(value)


# HASIL

print("Checksum Values:")
print(checksum)

print("\nTotal Checksum:", len(checksum))
