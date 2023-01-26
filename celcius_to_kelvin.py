#reference equation: 0°C + 273.15 = 273.15K

#Converts celcius to kelvin
def ctok(degrees_c):
    
    #Our equation
    Kelvin = float(degrees_c) + 273.15

    #Return Kelvin
    return Kelvin

#Test our equation
#Celcius is 0.0
ctok(0.0)
#Celcius is 37.0
ctok(37.0)
#Celcius is 99.0
ctok(99.0)
