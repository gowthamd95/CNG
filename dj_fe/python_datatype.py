# # Create list
# a = ['banana','1',"papaya","orange"] #single quotes, double quotes don't matter
# for i in a:
#     print(i)

# len_a = len(a)
# print(len_a)
# start = 0
# end = len_a
# step = 2

# for i in range(start,end,step):
#     print(a[i])


# a.append('cat')
# print(a)

# a = {}

# db['Omkar']['name'] 
# db[keys]['name']
# for keys in db:
#     if keys == 'Omkar':
#         print(db[keys]['name'])

# ## dict
# for x in range(3):
#     final_dict = {}
#     data_key = input("Enter pressure key: ")
#     data_value = input("Enter pressure value: ")
#     final_dict[data_key] = data_value
# print(final_dict)

# for x in range(3):    
#    pupils_dictionary = {}
#    new_key =input('Enter new key: ')
#    new_age = input('Enter new age: ')
#    pupils_dictionary[new_key] = new_age
# print(pupils_dictionary)
import pickle
filename = "/home/pi/cng/python_code_for_arduino/values.txt"
file_name = open(filename, 'rb')
new_values = pickle.load(file_name)
print(str(new_values))