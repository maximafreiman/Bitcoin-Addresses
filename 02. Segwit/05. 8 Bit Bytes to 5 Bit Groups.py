
# CONVERT 8-BIT BYTES -> 5-BIT GROUPS
# WITHOUT LIBRARY


# HASH160
h160_hex = "4f6e669e65be170eae07d9a7d81e181a9886fec3"


# STEP 1: HEX -> BYTE LIST

byte_list = []

for i in range(0, len(h160_hex), 2):
    hex_pair = h160_hex[i:i+2]
    byte_value = int(hex_pair, 16)
    byte_list.append(byte_value)

print("Byte List:")
print(byte_list)


# STEP 2: 8-BIT BYTES -> 5-BIT GROUPS

groups5 = []

acc = 0      # temporary bit storage
bits = 0     # number of bits currently stored

for b in byte_list:
    acc = (acc << 8) | b
    bits += 8

    while bits >= 5:
        bits -= 5
        value5 = (acc >> bits) & 31   # extract 5 bits
        groups5.append(value5)

# remaining bits (padding)
if bits > 0:
    value5 = (acc << (5 - bits)) & 31
    groups5.append(value5)


# RESULT

print("\n5-bit Groups (decimal):")
print(groups5)

print("\nTotal Groups:", len(groups5))
