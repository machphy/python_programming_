def add_key_value_pair(d, key, value):
    d[key] = value
    return d

my_dict = {"India": "New Delhi", "USA": "Wash"}
updated_dict = add_key_value_pair(my_dict, "Lucknow", "UP")


print("desh aur inke rajya name :-")
print(updated_dict)
