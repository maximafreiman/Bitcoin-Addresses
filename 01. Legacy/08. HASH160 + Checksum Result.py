hash160 = "4f6e669e65be170eae07d9a7d81e181a9886fec3"  # <------------ masukkan hash160 dari ripemd160
checksum = "9ba94fc0" # <------------ masukkan checksum dari hasil double_sha256

final_hex = hash160 + checksum  # menggabungkan hash160 + checksum

print("HASH160     :", hash160)
print("Checksum    :", checksum)
print("Final Hex   :", final_hex)
