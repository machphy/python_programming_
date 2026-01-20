original_list = [1, 2, [3, 4]]
new_list = original_list.copy()


new_list[0] = 99
new_list[2][0] = 100

print("Original List:", original_list)
print("New List:", new_list)
