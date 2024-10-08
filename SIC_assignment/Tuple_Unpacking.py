def tuple_sum_and_product(t):
    first_two_sum = t[0] + t[1]
    last_two_product = t[1] * t[2]
    return first_two_sum, last_two_product

test_tuple = (3, 4, 5)
sum_result, product_result = tuple_sum_and_product(test_tuple)
print("Sum of first two:", sum_result)
print("Product of last two:", product_result)
