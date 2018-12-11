# A. White December 10, 2018
# Part 10 of 1.2
# File: convertkilo-mi.py
# Converting kilometers to miles.

#defining variable.
def main():
    #telling reader what the script does.
    print("This program converts distances measured in kilometers to miles.")
    #asking reader the amount they want to convert.
    kilometers = eval(input("What is the distance in kilometers?"))
    #defining variable.
    miles = kilometers * .62
    #the output.
    print("The distance is", miles, "miles.")
    input("Press the <Enter> key to quit.")
          
main()
