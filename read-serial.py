import serial
import csv

arduino_port = "/dev/cu.usbmodem14201" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName= "ArduinoData.CSV" #name of the CSV file generated


ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)

file = open(fileName, "w")

samples = 10 #how many samples to collect
print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
while line <= samples:
    # incoming = ser.read(9999)
    # if len(incoming) > 0:
    if print_labels:
        if line==0:
            print("Printing Column Headers")
        else:
            print("Line " + str(line) + ": writing...")
    getData=str(ser.readline())
    data=getData[0:][:-2]
    print(data)

    file = open(fileName, "a")
    file.write(data + "\n") #write data with a newline
    line = line+1

file.close()
#if file.close():
print("Data collection complete!")
