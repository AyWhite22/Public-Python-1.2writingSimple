# A. White Dec 10, 2018
# December 10, 2018
# Part 9 of 1.2

#defining script.
def main():
    #telling reader what program does.
    print("This program converts a temperature in Fahrenheit to a temperature in Celcius.")
    #asking reader what amount they want to convert.
    fahrenheit = eval(input("What is the Fahrenheit temperature?"))
    #defining variables.
    celcius = 9/5 * fahrenheit + 32
    fahrenheit = (celcius - 32) * 5/9
    #the output.
    print("The temperature is", celcius, "degrees Celcius.")
    input("Press the <Enter> key to quit.")
main()
