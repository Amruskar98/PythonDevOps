# Example integers
a = 60  # In binary: 111100
b = 13  # In binary: 001101

# Bitwise AND (&)
and_result = a & b  # 60 & 13 = 12 (In binary: 001100)

# Bitwise OR (|)
or_result = a | b  # 60 | 13 = 61 (In binary: 111101)

# Bitwise XOR (^)
xor_result = a ^ b  # 60 ^ 13 = 49 (In binary: 110001)

# Bitwise NOT (~)
not_result_a = ~a  # ~60 = -61 (In binary: 11111111111111111111111111000011)
not_result_b = ~b  # ~13 = -14 (In binary: 11111111111111111111111111110011)

# Bitwise Left Shift (<<)
left_shift_result = a << 2  # 60 << 2 = 240 (In binary: 11110000)

# Bitwise Right Shift (>>)
right_shift_result = a >> 2  # 60 >> 2 = 15 (In binary: 00001111)

# Print results
print("a & b:", and_result)
print("a | b:", or_result)
print("a ^ b:", xor_result)
print("~a:", not_result_a)
print("~b:", not_result_b)
print("a << 2:", left_shift_result)
print("a >> 2:", right_shift_result)
