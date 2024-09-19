person={
    "name":"kuchbhi",
    "age":30,
    "city":"new yerk"
}

squares = {x: x*x for x in range(6)}

# Dictionary comprehension with a condition
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 845454: 64}
