import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-a", "--numa", dest="num1", help="Enter a Number: ")
parser.add_option("-b", "--numb", dest="num2", help="Enter Second Number: ")

(option, arguments)= parser.parse_args()

num1 = 20
num2 = 0

try:
    subprocess.run(["sudo","ifconfig","numa"],check=True)
    subprocess.run(["sudo","ifconfig",])


print(option)
print(arguments)
print (num1 / num2)



