import os

memory_addresses_occupied = []

def initialise_ram():
    if os.path.exists("ram"):
        os.remove("ram")
    else:
        fh = open("ram", "w+")
        fh.close()