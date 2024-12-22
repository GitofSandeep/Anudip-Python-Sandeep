""" Question:
Write a program to input the temperature in Celsius
and calculate and print it in Fahrenheit. """

# take celcius degree from user
celcius = int(input("Enter the Celcius temperature: "))

# convert it to fahrenheit
fahrenheit = (celcius * 9/5) + 32
print("The temperature in Fahrenheit is ", fahrenheit)