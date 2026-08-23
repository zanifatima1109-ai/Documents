import subprocess
import optparse

def mac_changer(adopter, new_MAC):
        print("[+] Changing MAC address for "+ adopter +" to " + new_mac)
        subprocess.run(["sudo","ifconfig",adopter,"down"],check=True)
        subprocess.run(["sudo","ifconfig",adopter,"hw","ether",new_mac],check=True)
        subprocess.run(["sudo","ifconfig",adopter,"up"],check=True)
        print("[+] Done.")

parser =optparse.OptionParser()
parser.add_option('-i','--interface', dest="interface",help="Interface to change its MAC address ")
parser.add_option('-m','--mac', dest="new_mac",help="new MAC address")

(option, args) = parser.parse_args()

interface = option.interface 
new_mac = option.new_mac

if not interface and not new_mac:
    if not interface:
          interface = input("[-] please specify an interface, use --help for more info:")
if not new_mac:
      new_mac = input("[-] please specify a new MAC address , use --help for more info:" )



