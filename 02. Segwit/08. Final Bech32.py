# -----------------------------------------
# FINAL BECH32 ADDRESS
# WITHOUT LIBRARY
# -----------------------------------------

# payload data (with witness version)
data = [
    0, 9, 29, 23, 6, 13, 7, 19, 5, 23, 24,
    11, 16, 29, 11, 16, 7, 27, 6, 19, 29,
    16, 7, 16, 24, 3, 10, 12, 8, 13, 31,
    22, 3
]

# checksum result
checksum = [4, 16, 3, 22, 11, 1]

# Bech32 charset
charset = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"

# -----------------------------------------
# STEP 1: COMBINE DATA + CHECKSUM
# -----------------------------------------
combined = data + checksum

# -----------------------------------------
# STEP 2: CONVERT VALUES TO CHARACTERS
# -----------------------------------------
encoded = ""

for value in combined:
    encoded += charset[value]

# -----------------------------------------
# STEP 3: ADD PREFIX
# -----------------------------------------
address = "bc1" + encoded

# -----------------------------------------
# RESULT
# -----------------------------------------
print("Final Bech32 Address:")
print(address)
