# A. White, Dec 10, 2018
# File: convert3.py
# Part 5 of 1.2
# A program to compute and print a table of Celsius temperatures and
#the Fahrenheit equivalents every 10 degrees
#from 0 degrees celsius to 100 degrees celsius

#defining the script 
def main():
    print("Celisus Temperatures and")
    print("Their Fahrenheit Equivalents")
    print("{0:<14}{1:<14}".format("C", "F"))
    print("----------------------------")
    #Listing celcius from 0 degrees to 100 degrees.
    for i in range(11):
        celsius = 10 * i
        #formula for converting fahrenheit to celcius.
        fahrenheit = int(9/5 * celsius + 32)
         #Making the table.
        print("{0:<14}{1:<14}".format(celsius, fahrenheit))
        
main()
