import subprocess
from termcolor import colored


def nmap_simple():
    print(colored("Der Chef scannt mit!", "yellow", "on_grey"))
    print()
    print("input IP:")
    ip_addr = input("> ")
    print(colored("Wenn der Scanner fertig is, gibt's erstmal ne Currywurst!",
                  "yellow", "on_grey"))
    subprocess.run(["nmap", ip_addr])   # run nmap with ip
    # look for output
    print()
    input(colored("Scan beendet, der Chef geht jetzt Bier holen!",
                  "yellow", "on_grey"))
