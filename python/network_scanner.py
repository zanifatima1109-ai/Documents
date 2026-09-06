from scapy.all import IP, TCP, sr1

# List
ports = [21, 22, 23, 25, 53, 80, 443]

# Tuple
target = ("127.0.0.1",)

# Dictionary
port_names = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

print("Simple Python Port Scanner")

for port in ports:

    packet = IP(dst=target[0]) / TCP(dport=port, flags="S")

    answer = sr1(packet, timeout=1, verbose=0)

    if answer:
        print("Port", port, port_names[port], "is OPEN")

    else:
        print("Port", port, port_names[port], "is CLOSED")




        