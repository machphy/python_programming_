def sumoftuple(t):
    first_sum = t[0] + t[1]
    last_product = t[1] * t[2]
    return first_sum, last_product

test_tuple = (3, 4, 5)
sum_result, product_result = sumoftuple(test_tuple)
print("Sum of first two:", sum_result)
print("Product of last two:", product_result)
