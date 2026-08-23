import subprocess
import optparse



"""
comments 
"""
'''
comments 
'''

parser =optparse.OptionParser()

parser.add_option('-i','--interface', dest="interface",help="enter network abopter")
parser.add_option('-m','--mac', dest="new_mac",help="enter new mac address")
parser.add_option('-n',"--name", dest="name",help="enter your name")

                  
(option, arguments) = parser.parse_args()

print(option)
print(arguments)

interface = option.interface
new_mc = option.new_mac


new_mac = input("Enter New Mac Address:")
interface = input("Which Interface to Use?")

try:

    subprocess.run(["sudo","ifconfig",interface],check=True)
    subprocess.run(["sudo","ifconfig",interface,"down"],check=True)
    subprocess.run(["sudo","ifconfig",interface,"hw","ether",new_mac],check=True)
    subprocess.run(["sudo","ifconfig",interface,"up"],check=True)
    subprocess.run(["sudo","ifconfig",interface],check=True)
except:
    print("Error")

