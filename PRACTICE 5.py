
celsius_temps = [0, 33, 27, 80, -15]

celsius_to_fahrenheit = lambda c: c * 9/5 + 32

fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))


print("Celsius Temperatures:", celsius_temps)
print("Fahrenheit Temperatures:", fahrenheit_temps)