data_hex = "004f6e669e65be170eae07d9a7d81e181a9886fec39ba94fc0"

alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

# hex -> integer
num = int(data_hex, 16)

# konversi ke base58
encoded = ""

while num > 0:
    num, rem = divmod(num, 58)
    encoded = alphabet[rem] + encoded

# cek leading zero byte ("00")
# setiap 00 di depan = tambah "1"
leading_zero_bytes = 0

for i in range(0, len(data_hex), 2):
    if data_hex[i:i+2] == "00":
        leading_zero_bytes += 1
    else:
        break

encoded = ("1" * leading_zero_bytes) + encoded

print(encoded)
