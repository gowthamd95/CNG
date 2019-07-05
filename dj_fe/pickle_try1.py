
# import pickle 

# Pdata = int(input('Enter pressure data: '))
# data = []
# for i in range(Pdata):
#     raw=input('Enter data '+str(i)+' : ')
#     data.append(raw)

# file = open('important', 'wb')
# pickle.dump(data, file)
# file.close()
# file = open('important', 'wb')
# data = pickle.load(file)
# for keys in data:
#     print(keys, '=>', data[keys])
# file.close

# def storeData(): 
#     # initializing data to be stored in db 
#     Gas = {'g1' : 40, 'g2' : 50, 
#     'g3' : 55, 'g4' : 60, 'g5' : 45} 
#     Pressure = {'p1' : 8, 'p2' : 9, 
#     'p3' : 10} 
  
#     # database 
#     db = {} 
#     db['Gas'] = Gas 
#     db['Pressure'] = Pressure 
      
#     # Its important to use binary mode 
#     dbfile = open('examplePickle1', 'ab') 
      
#     # source, destination 
#     pickle.dump(db, dbfile)                      
#     dbfile.close() 
  
# def loadData(): 
#     # for reading also binary mode is important 
#     dbfile = open('examplePickle1', 'rb')      
#     db = pickle.load(dbfile) 
#     for keys in db: 
#         print(keys, '=>', db[keys]) 
#     dbfile.close() 
  
# if __name__ == '__main__': 
#     storeData() 
#     loadData() 


#input data
import pickle

# data = []
# pressure_values = int(input('input data: '))
# data.append(pressure_values)
#data = {}
#works
# data = dict()
# key = input("enter the key: ")
# value = input("enter the value: ")

# data[key] = value
# print(data)

#new

# import pickle 

# pressure_values = { 'p1':[7,8,9],
#                     'p2':[3,45,5],
#                     'p3':[9,10,10]
#                    }

# #to replace one value with another
# pressure_values['p1'][-2]=999

# #l0ading files
# filename = "pvalues.txt"
# file = open(filename, 'wb')
# pickle.dump(pressure_values, file)



# #0pen file
# file = open(filename, 'rb')
# new_values = pickle.load(file)

# print("p1 pressure_values: ", new_values)

#############
# #code that works
# import pickle

# class_list = dict()
# data = input('Enter pressure value & gas value by ":" ')
# temp = data.split(':')
# class_list[temp[0]] = int(temp[1])
 
# # Displaying the dictionary

# #l0ading files
# filename = "values.txt"
# file = open(filename, 'wb')
# pickle.dump(data, file)
# #0pen file
# file = open(filename, 'rb')
# new_values = pickle.load(file)

# for key, value in class_list.items():
# 	print('Pressure_value: {}, Gas_value: {}'.format(key, value))


#multiple inputs to dict

final_dict = {}
for x in range(3):
    #final_dict = {}
    data_key = input("Enter pressure key: ")
    data_value = input("Enter pressure value: ")
    # if data_keynot in final_dict:
    #     final_dict[data_key]=''
    # else:
    final_dict[data_key] = data_value
for x in range(5):
    #final_dict = {}
    data_key = input("Enter Gas key: ")
    data_value = input("Enter Gas value: ")
    # if data_keynot in final_dict:
    #     final_dict[data_key]=''
    # else:
    final_dict[data_key] = data_value
filename = "/home/gowtham/CNG/mysite/values.txt"
file = open(filename, 'wb')
pickle.dump(final_dict, file)
print(final_dict)
