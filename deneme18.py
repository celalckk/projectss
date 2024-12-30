def CelciusToFahrenheit(Celsius):
    Fahrenheit = Celsius * 1.8 + 32
    return Fahrenheit


degreeGet = float(input("please enter the number as celcius:"))
print("fahrenheit: ",CelciusToFahrenheit(degreeGet)) 