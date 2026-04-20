# -----------------------------------------
# ADD WITNESS VERSION
# WITHOUT LIBRARY
# -----------------------------------------

# 5-bit groups result
groups5 = [
    9, 29, 23, 6, 13, 7, 19, 5,
    23, 24, 11, 16, 29, 11, 16, 7,
    27, 6, 19, 29, 16, 7, 16, 24,
    3, 10, 12, 8, 13, 31, 22, 3
]

# witness version for Native SegWit
witness_version = 0

# add version at front
data = [witness_version] + groups5

# -----------------------------------------
# RESULT
# -----------------------------------------
print("Data With Witness Version:")
print(data)

print("\nTotal Values:", len(data))
