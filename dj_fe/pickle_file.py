import pickle
value_dict = {
    "pressure1": 74,
    "pressure2": 74,
    "pressure3": 774,
    }

filename = "values_1.txt"
file = open(filename, 'wb')
pickle.dump(value_dict, file)
print(value_dict)