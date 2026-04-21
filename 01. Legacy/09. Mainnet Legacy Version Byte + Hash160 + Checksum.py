# Tambahkan version byte 00 + HASH160 + checksum
# tanpa library sama sekali

hash160  = "4f6e669e65be170eae07d9a7d81e181a9886fec3"
checksum = "9ba94fc0"

version_byte = "00"  # tambahkan version "00"



final_hex = version_byte + hash160 + checksum     # gabungkan semuanya

print("Version Byte :", version_byte)
print("HASH160      :", hash160)
print("Checksum     :", checksum)
print("Final Hex    :", final_hex)
