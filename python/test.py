import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-f", "--first", dest="first_name", help="First Name")
parser.add_option("-l", "--last", dest="last_name", help="Last Name")
parser.add_option("-a", "--age", dest="age", help="Age")

(options, arguments) = parser.parse_args()

print("First Name:", options.first_name)
print("Last Name:", options.last_name)
print("Age:", options.age)


