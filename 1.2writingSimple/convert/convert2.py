# A. White December 10, 2018
# Part 4 of 1.2
# File: convert2.py
# Loop script

#defining the script.
def main():
    #running the script 5 times.
    for i in range(5):
        #the formula for converting celcius to fahrenheit.
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        #printing out the amount the expression comes to.
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
