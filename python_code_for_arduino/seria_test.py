import serial
import pickle
index = 0
value_dict = {
        "P1": 78,
        "P2": 79,
        "P3": 77,
        "G1": 78,
        "G2": 66,
        "G3": 40,
        "G4": 75,
        "G5": 24,
        }
ser = serial.Serial('/dev/ttyACM2',9600)
serialCount = list()
def storeVariable(listCount):
    j = ""
    for i in listCount:
        if i.isdigit():
            j = j + i
    return int(j)

while True:
    val1 = val2 = val3 = []
    serialCount.append(ser.read())
    for i in serialCount:
        if i == "-":
            val1 = serialCount
            serialCount = list()
        if i == "*":
            val2 = serialCount
            serialCount = list()
        if i == "#":
            val3 = serialCount
            serialCount = list()
    if val1:
        print ("val1 rec is : " + str(storeVariable(val1)))
        rec_val1 = storeVariable(val1)
        value_dict["P1"] = int("".join(val1[:-1]))
    if val2:
        print ("val2 rec is : "+str(storeVariable(val2)))
        rec_val2 = storeVariable(val2)
        value_dict["P2"] = int("".join(val2[:-1]))
    if val3:
        print("val3 rec is :  " + str(storeVariable(val3)))
        rec_val3 = storeVariable(val3)
        value_dict["P3"] = int("".join(val3[:-1]))
        
    ##file upload
    filename = "values.txt"
    file = open(filename, 'wb')
    pickle.dump(value_dict, file)
    print(value_dict)
