# RIPEMD160 hash dalam bentuk hex string
h160_hex = "4f6e669e65be170eae07d9a7d81e181a9886fec3"

byte_list = []

for i in range(0, len(h160_hex), 2):
    pasangan_hex = h160_hex[i:i+2]      # ambil 2 karakter
    nilai_byte = int(pasangan_hex, 16)  # hex ke integer 0-255
    byte_list.append(nilai_byte)

# tampilkan hasil
print("Bytes (decimal):")
print(byte_list)

print("\nBytes (hex):")
for b in byte_list:
    print(format(b, "02x"), end=" ")

print("\n\nTotal byte:", len(byte_list))
