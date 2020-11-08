import serial

arduino_port = "/dev/cu.usbmodem14101" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="analog-data.csv" #name of the CSV file generated

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created file")

#display the data to the terminal
getData=str(ser.readline())
data=getData[0:][:-2]
print(data)

#add the data to the file
file = open(fileName, "a") #append the data to the file
file.write(data + "\n") #write data with a newline

#close out the file
file.close()

samples = 10 #how many samples to collect
print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
while line <= samples:
    # incoming = ser.read(9999)
    # if len(incoming) > 0:
    if print_labels:
        if line==0:
            # print("Line " + str(line) + ": writing...")
            getData= str(ser.readline()
            data = getData[0:][:-2]
            print(data)



    file = open(fileName, "a")
    file.write(data + "\n") #write data with a newline
    line = line+1

print("Data collection complete!")
file.close()
