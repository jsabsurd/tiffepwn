import subprocess

def nmap_simple():
    print("input IP:")
    ip_addr = input("> ")
    subprocess.run(["nmap", ip_addr])   # run nmap with ip
    # look for output
    print()
    input("press enter to return to menu.")
