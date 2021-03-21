# author: Michał Rybiński
# nickname: rybinskm
# date of create: 21-03-2021

import pyperclip

proxi = "2E 00 32 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99"
space = " "

debug_list = []
proxi_list = []
proxi_without_debug_list = []

# def gen_proxi():
#     global generated_proxi, length
#     length = 99 #int(input("Set PROXI length: "))
#     for i in range(length):
#         if i < 9:
#             generated_proxi.append(f"0{i+1}")
#         else:
#             generated_proxi.append(f"{i+1}")
#     print(f"{generated_proxi}")

def proxi_new():
    proxi_length = len(proxi.split(' '))
    for i in range(proxi_length):
        byte = proxi.split(' ')[i]
        proxi_list.append(byte)

    debug_list = proxi_list[0:3]
    proxi_without_debug_list = proxi_list[3:]
    #print(f"{proxi_list}")
    #print(f"{debug_list}")

    byte_to_change = 35-1  #int(input("Byte number: ")) - 1
    new_value = "4E" #str(input("New hex value: "))
    proxi_without_debug_list[byte_to_change] = new_value

    # for i in range(proxi_length):
    #     byte = proxi_without_debug.split(" ")[i]
    #     proxi_without_debug_list.append(byte)

    proxi_to_crccalc = space.join(proxi_without_debug_list[25:])
    print(f"{proxi_to_crccalc}")

    crc_params = "51435"  # str(input("CRC params: "))

    for i in range(9, 14):
        #print(f"{proxi_without_debug_list[i]}")
        proxi_without_debug_list[i] = f"3{crc_params[i-9]}"
        #print(f"{proxi_without_debug_list[i]}")

    proxi_without_debug = space.join(proxi_without_debug_list)
    print(f"{proxi_without_debug}")

    debug = space.join(debug_list)
    print(f"{debug}")

    #proxi_without_debug = space.join(generated_proxi)
    #print(f"{proxi_without_debug}")

    proxi_full = debug + space + proxi_without_debug
    print(f"{proxi_full}")
    pyperclip.copy(str(proxi_full))

#gen_proxi()
proxi_new()