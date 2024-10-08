def add_key_value_pair(d, key, value):
    d[key] = value
    return d

my_dict = {"India": "New Delhi", "USA": "Washington D.C."}
updated_dict = add_key_value_pair(my_dict, "Canada", "Ottawa")
print(updated_dict)
