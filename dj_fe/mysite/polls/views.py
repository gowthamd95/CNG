from django.shortcuts import render
import pickle

# Create your views here.
from django.http import HttpResponse


def convert_percent(val):
    return [100-((val/1023)*100), (val/1023)*100]

def index(request):
    # class_list = dict()
    # pressure1 = int(request.GET.get('P1',0))
    # pressure2 = int(request.GET.get('P2',0))
    # pressure3 = int(request.GET.get('P3',0))
    # gas1 = int(request.GET.get('G1',0))
    # gas2 = int(request.GET.get('G2',0))
    # gas3 = int(request.GET.get('G3',0)) 
    # gas4 = int(request.GET.get('G4',0))
    # gas5 = int(request.GET.get('G5',0))
    # class_list["P1"] = int(pressure1)
    # class_list["P2"] = int(pressure2)
    # class_list["P3"] = int(pressure3)
# Displaying the dictionary
    #l0ading files
    filename = "/home/pi/cng/python_code_for_arduino/values.txt"
    # file_name = open(filename, 'wb')
    # pickle.dump(class_list, file_name)
   #0pen file
    file_name = open(filename, 'rb')
    new_values = pickle.load(file_name)
    pressure1 = new_values['P1']
    pressure2 = new_values['P2']
    pressure3 = new_values['P3']
    gas1 = new_values['G1']
    gas2 = new_values['G2']
    gas3 = new_values['G3'] 
    gas4 = new_values['G4']
    gas5 = new_values['G5']
    # return HttpResponse(str(new_values))
    # return HttpResponse(str(class_list))
    return render(request,'dashboard.html', {"pressure_val1":convert_percent(pressure1), "pressure_val2":convert_percent(pressure2), "pressure_val3":convert_percent(pressure3), "gas_val1":convert_percent(gas1), "gas_val2":convert_percent(gas2),"gas_val3":convert_percent(gas3), "gas_val4":convert_percent(gas4), "gas_val5":convert_percent(gas5)})
    
def input(request):
    #0pen file
    class_list = dict()
    pressure1 = int(request.GET.get('P1',0))
    pressure2 = int(request.GET.get('P2',0))
    pressure3 = int(request.GET.get('P3',0))
    gas1 = int(request.GET.get('G1',0))
    gas2 = int(request.GET.get('G2',0))
    gas3 = int(request.GET.get('G3',0)) 
    gas4 = int(request.GET.get('G4',0))
    gas5 = int(request.GET.get('G5',0))
    class_list["P1"] = int(pressure1)
    class_list["P2"] = int(pressure2)
    class_list["P3"] = int(pressure3)
    class_list["G1"] = int(pressure1)
    class_list["G2"] = int(pressure2)
    class_list["G3"] = int(pressure3)
    class_list["G4"] = int(pressure1)
    class_list["G5"] = int(pressure2)
    filename = "values.txt"
    file_name = open(filename, 'wb')
    pickle.dump(class_list, file_name)
    return HttpResponse("SUCCESS")



# final_dict = {}
# for x in range(3):
#     #final_dict = {}
#     data_key = input("Enter pressure key: ")
#     data_value = input("Enter pressure value: ")
#     final_dict[data_key] = data_value
# print(final_dict)

