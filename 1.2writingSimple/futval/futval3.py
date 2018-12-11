# futval3.py
# A program to compute the future value of an investment
#with number of years determined by the user.
# A. White
# December 10, 2018
# Part 7 of 1.2

#defining the script.
def main():
    #telling the reader what this script does.
    print("This program calculates the total future value")
    print("of a multi-year investment with non-compounding interest")
    print("and an additional investment of a certain fixed amount each year.")
#making principal a variable.
    principal = eval(input("Enter the initial principal: "))
#making apr a variable.    
    apr = eval(input("Enter the annual interest rate: "))
#making yearly investment a variable.
    yearlyinvestment = eval(input("Enter the fixed yearly amount to invest:"))
#making years a variable.
    years = eval(input("Enter the number of years for the investment:"))
#the equation to figure out the value. 
    for i in range(years):
          principal = principal + yearlyinvestment
          principal = principal * (1 + apr)
#prints out the value using the equation above.
    print("The value in ", years ,"years is:", principal, sep=" ")

main()
