# Read from memory

def read_ram(memory_address):
    target = f"{memory_address:08X}"

    fh = open("ram", "r")
    lines = fh.readlines()
    fh.close()

    for line in lines:
        if line[:8] == target:
            return line[8:]