import pyperclip

# "2E 00 32" - debug to send proxi
proxi = "A0 0D D5 2E 5F FF F8 C2 DD 90"
proxi_list = []
proxi_list_new = []
proxi_out = str

def read_byte():
    global proxi, proxi_list
    #print(hex(0xFF))
    print(len(proxi.split(' ')))
    print(proxi.split(' '))
    for i in range(len(proxi.split(' '))):
        param = proxi.split(' ')[i]
        param_int = int(param, 16)
        #print(param_int)
        param_hex = hex(param_int)
        #print(param_hex)
        proxi_list.append(param_hex)
        proxi_list_new.append(param_hex)
    print(f"{proxi_list}")
    byte = int(input("Byte number: "))
    print(f"{proxi_list[byte]}")
    new_value = int(input("New value: "), 16)
    new_value_hex = hex(new_value)
    proxi_list_new[byte] = new_value_hex
    for i in range(len(proxi)):
        proxi_out.

    print(f"Previous proxi: {str(proxi)}")
    print(f"New proxi: {str(proxi_list_new)}")
    pyperclip.copy(str(proxi_out))

read_byte()

# h = "0xB1"
# h_int = int(h, 16)
# h_hex = hex(h_int)
# print(h_hex)