import tkinter as tk
from tkinter import messagebox


pressure_sensor_values = [{'value':23,'row':1,'column':1},{'value':23,'row':2,'column':2},{'value':23,'row':3,'column':2}]
gas_sensor_values = [{'value':23,'row':1,'column':4},{'value':23,'row':2,'column':4},{'value':23,'row':3,'column':4},{'value':23,'row':4,'column':4}]
root = tk.Tk()
pressure_sensor = ['P1','P2','P3']

root.geometry("500x500")

for i in range(0,len(pressure_sensor_values)):
	button = tk.Button(root, text =str(pressure_sensor_values[i]['value']), fg="blue", bg="yellow")
	button.grid(row=pressure_sensor_values[i]['row'], column=pressure_sensor_values[i]['column'])

for j in range(0,len(gas_sensor_values)):
	button = tk.Button(root, text =str(gas_sensor_values[j]['value']))
	button.grid(row=gas_sensor_values[j]['row'], column=gas_sensor_values[j]['column'])





root.mainloop()