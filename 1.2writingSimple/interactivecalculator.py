# A. White December 10, 2018
# Part 12 of 1.2
# File: interactivecalculator.py
# A calculator that the reader can interact with.

#defining the script.
def main():
#telling the reader what the script does.
    print("This program is an interactive calculator. You can run up to 100 expressions. Enter your calculations below.")
#this will make the script run 100 times.
    for i in range(100):
#this is letting the computer read the expression.
        expression = eval(input(""))
#telling the computer to print out the answer to the reader's expression.
        print(expression)
        input("To quit early enter an invalid expression")
main()
