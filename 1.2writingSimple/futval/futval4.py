# A. White Dec 10, 2018
# Part 8 of 1.2
# futval4.py

#defining the script.
def main():

#telling the reader what the script does.
    print("This program calculates the total future value of a multi-year ")
    print("investment with by describing the interest accrued")
    print("in terms of a nominal rate and the number of")
    print("compounding periods.")
#telling the reader what to input and defining variables.
    principal = eval(input("Enter the initial principal: "))
    interestrate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years for the investment: "))
#the equation being used to figure out nominal rate.
    nominalrate = interestrate / periods
#the equation being used to figure out the principal variable.          
    for i in range(periods * years):
          principal = principal * (1 + nominalrate)
#telling the script to output the value of interests in that amount of years.
    print("The value in ", years ,"years is:", principal, sep=" ")
main()
