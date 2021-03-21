import pyperclip

proxi = ""
space = " "

debug_list = []
proxi_list = []
proxi_without_debug_list = []

def proxi_new():
    proxi_length = len(proxi.split(' '))
    for i in range(proxi_length):
        byte = proxi.split(' ')[i]
        proxi_list.append(byte)

    debug_list = proxi_list[0:3]
    proxi_without_debug_list = proxi_list[3:]

    byte_to_change = int(input("Byte number: ")) - 1
    new_value = str(input("New hex value: "))
    proxi_without_debug_list[byte_to_change] = new_value

    proxi_to_crccalc = space.join(proxi_without_debug_list[25:])
    print(f"{proxi_to_crccalc}")
    pyperclip.copy(str(proxi_to_crccalc))
    print("Relevant part of the PROXI data has been copied to the clipboard.")

    crc_params = str(input("CRC params: "))  # "51435"

    for i in range(9, 14):
        proxi_without_debug_list[i] = f"3{crc_params[i-9]}"

    proxi_without_debug = space.join(proxi_without_debug_list)
    print(f"{proxi_without_debug}")

    debug = space.join(debug_list)
    print(f"{debug}")

    proxi_full = debug + space + proxi_without_debug
    print(f"{proxi_full}")
    pyperclip.copy(str(proxi_full))
    print("New PROXI data has been copied to the clipboard.")

proxi_new()
