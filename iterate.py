import argparse

parser = argparse.ArgumentParser()
parser.add_argument ('--number', help = "enter the numbers")
args = parser.parse_args()
num = list(range(10))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum))
    previousNum=i
