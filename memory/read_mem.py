# Read from memory

def read_ram(memory_address):
    target = f"0x{memory_address:08X}"

    fh = open("ram", "r")
    lines = fh.readlines()
    fh.close()

    for line in lines:
        if line[:10] == target:
            return line[10:]