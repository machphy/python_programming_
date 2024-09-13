A = {5, 14, 0, 12, 0, 12, 0, 4, 52, 1, 1, 6, 31, 5}
B = {3, 4, 6, 4, 84, 6, 58, 5, 64, 3, 6, 4, 8, 6, 5}

# Performing set operations
c = A & B  # Intersection
s = A | B  # Union
k = A ^ B  # Symmetric difference

# Printing results
print("Intersection (A & B):", c)
print("Union (A | B):", s)
print("Symmetric difference (A ^ B):", k)
