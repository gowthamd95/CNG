import serial
index = 0
ser = serial.Serial('/dev/ttyACM0',9600)
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
        print ("Val1 rec is : " + str(storeVariable(val1)))
        rec_val1 = storeVariable(val1)
    if val2:
        print ("Val2 rec is : "+str(storeVariable(val2)))
        rec_val2 = storeVariable(val2)
    if val3:
        print("Val3 rec is :  " + str(storeVariable(val3)))
        rec_val3 = storeVariable(val3)
        
