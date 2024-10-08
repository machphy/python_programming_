def tuples_to_dict(tuples_list):
    return {name: age for name, age in tuples_list}


name_age_tuples = [("John", 25), ("Jane", 22), ("Doe", 30)]
print(tuples_to_dict(name_age_tuples))
