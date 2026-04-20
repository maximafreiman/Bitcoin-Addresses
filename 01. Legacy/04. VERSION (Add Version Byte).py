# TAMBAHKAN VERSION BYTE ('00' UNTUK MAINNET LEGACY)


hash160_hex = "4f6e669e65be170eae07d9a7d81e181a9886fec3"

# convert ke bytes
hash160 = bytes.fromhex(hash160_hex)

# version byte (mainnet)
version = b'\x00'

# gabung
payload = version + hash160

print("Version + HASH160:")
print(payload.hex())
