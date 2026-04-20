# Ambil checksum Bitcoin dari hasil double SHA256. Tulis hasil hash sebelumnya di double_sha256 = ....

double_sha256 = "9ba94fc04b8c1b3f138f881c4756ad4b6a60140f0bb43ab671a94665b92398a5"

# checksum = 4 byte pertama = 8 karakter hex pertama
checksum = double_sha256[:8]

print("Checksum:", checksum)
