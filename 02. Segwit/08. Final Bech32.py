# FINAL BECH32 ADDRESS
# NO LIBRARY
# -----------------------------------------

# payload data (+ witness version)
data = [
    0, 9, 29, 23, 6, 13, 7, 19, 5, 23, 24,
    11, 16, 29, 11, 16, 7, 27, 6, 19, 29,
    16, 7, 16, 24, 3, 10, 12, 8, 13, 31,
    22, 3
]

# checksum result
checksum = [4, 16, 3, 22, 11, 1]

# Bech32 charset (udah standard dari Pieter Wuille dan Gregory Maxwell)
charset = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"


# STEP 1: COMBINE DATA + CHECKSUM

combined = data + checksum


# STEP 2: konversi nilai ke karakter

encoded = ""

for value in combined:
    encoded += charset[value]


# STEP 3: TAMBAHKAN PREFIX

address = "bc1" + encoded


# RESULT (ADDRESS SEGWIT NIH BOSS!!)

print("Final Bech32 Address:")
print(address)
