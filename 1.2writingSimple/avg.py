# avg.py
# by A. White Dec. 10, 2018
# A simple program to average three exam scores.
# Illustrates use of multiple input
def main():
    #This is an introduction
    print("This program computes the average of three exam scores. ")

    #This is an input
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    #This is an output
    print("The average of the scores is: ", average)

main()
