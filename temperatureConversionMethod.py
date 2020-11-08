def getTemperatureFromUSDAScale(scale):
    values = {1: -51.1,
              2: -45.6,
              3: -40,
              4: -34.4,
              5: -28.9,
              6: -23.3,
              7: -17.8,
              8: -12.2,
              9: -6.7,
              10: -1.1,
              11: 4.4,
              12: 10
              }
    return values[scale]

def convertCelciusToFarenheight(temp):
    return temp*(9/5) + 32
