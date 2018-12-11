# futval2.py
# A program to compute the future value of an investment
#with number of years determined by the user.
# Part 6 of 1.2

#defining the script.
def main():
    #telling the reader what the script does.
    print("This program calculates the future value")
    print("of a multi-year investment with non-compounding interest.")
    #making principal a variable.  
    principal = eval(input("Enter the initial principal: "))
    #making apr a variable.
    apr = eval(input("Enter the annual interest rate: "))
    #making years a variable.
    years = eval(input("Enter the number of years for the investment: "))
    #setting up the principal variable.
    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in ", years ,"years is:", principal)

main()
