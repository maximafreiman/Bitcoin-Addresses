# VERSION + HASH160 (HASH160: HASIL HASH DARI RIPEMD160)
# SIMULASI HASHING DAN RINGKASKAN HASIL SHA256 
# JANGAN PERNAH KIRIM BITCOIN DARI ADDRESS UTAMA ANDA KE ADDRESS EKSPERIMENTAL INI KALAU MAU SIMULASI KIRIM DI HASIL AKHIR!!!
# JANGAN PERNAH PAKAI PRIVATE KEY INI DI WALLET ANDA!!! KARENA SUDAH TERSEBAR DI INTERNET
# MOHON BIJAK. INI HANYA EDUKASI SEMATA



# === VERSION BYTE + HASH160 ===

## <---- Masukkan data (HASH160 hex, hasil RIPEMD160) disini
hash160_hex = "4f6e669e65be170eae07d9a7d81e181a9886fec3"


# === VALIDASI INPUT ===
if len(hash160_hex) != 40:
    raise ValueError("HASH160 harus 20 byte (40 hex karakter)")      ### RIPEMD160 = 160 bit = 20 byte


# === CONVERT ===
hash160 = bytes.fromhex(hash160_hex)                                 ### ubah hex → bytes


# === VERSION BYTE ===
version = b'\x00'                                                    ### 0x00 = Bitcoin mainnet (P2PKH)


# === GABUNG ===
payload = version + hash160                                          ### ini disebut payload address


print("=== VERSION + HASH160 ===")
print(payload.hex())     
