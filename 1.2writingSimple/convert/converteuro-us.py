# A. White December 10, 2018
# Part 11 of 1.2
# File: converteuro-us.py
# Converting Euros to US dollars

#defining script.
def main():
    #telling reader what the program does.
    print("This program converts Euros to US Dollars.")
    print("")
    #asking reader the amount they want to convert.
    euro = eval(input("What is the amount of Euros?"))
    #defining variable.
    USD = euro * 1.14
    #the output.
    print("")
    print("This equals", USD, "dollars.")
    input("Press the <Enter> key to quit.")
main()
