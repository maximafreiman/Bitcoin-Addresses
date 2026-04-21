double_sha256 = "9ba94fc04b8c1b3f138f881c4756ad4b6a60140f0bb43ab671a94665b92398a5"  # <--------------- Ambil checksum Bitcoin dari hasil double SHA256. 


checksum = double_sha256[:8] # checksum = 4 byte pertama = 8 karakter hexadecimal pertama

print("Checksum:", checksum)
