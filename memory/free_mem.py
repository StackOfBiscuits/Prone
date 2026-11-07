# Free memory

import initialise_ram

def free_ram(memory_address):
    target = f"0x{memory_address:08X}"

    with open("ram", "r") as file:
        lines = file.readlines()

    with open("ram", "w") as file:
        for line in lines:
            stored_address = line[:10]

            if stored_address != target:
                file.write(line)

    initialise_ram.memory_addresses_occupied.remove(memory_address)