# Write to memory

import initialise_ram

def write_to_ram(contents):
    new_mem_addr = 0
    current_ram_maddr = initialise_ram.memory_addresses_occupied

    ascii_text = contents.encode("ascii", errors="ignore").decode("ascii")
    hex_value = ascii_text.encode("utf-8").hex()

    if current_ram_maddr: 
        for i in range(1, len(current_ram_maddr)):
            if (current_ram_maddr[i] - current_ram_maddr[i-1] > 1):
                new_mem_addr = current_ram_maddr[i-1] + 1
        if new_mem_addr == 0:
            new_mem_addr = current_ram_maddr[-1] + 1

        formatted_address = f"0x{new_mem_addr:08X}"


    formatted_address = f"0x{new_mem_addr:08X}"
    fh = open("ram", "a")
    fh.write(f"{formatted_address}{hex_value}\n")
    fh.close()

    initialise_ram.memory_addresses_occupied.append(new_mem_addr)

