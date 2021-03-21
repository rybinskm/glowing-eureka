import pyperclip

set_proxi = "2E 00 32 " # debug to send proxi
proxi = "A0 0D D5 2E 5F FF F8 C2 DD 90"
proxi_list = []
proxi_list_new = []
space = " "

def proxi_editor():
    global proxi, proxi_int
    proxi_length = len(proxi.split(' '))
    print(f"Proxi length: {proxi_length}")
    for i in range(proxi_length):
        param = proxi.split(' ')[i]
        proxi_list.append(param)
        proxi_list_new.append(param)
    #print(f"{proxi_list}")
    #print(f"{proxi_list_new}")
    byte = int(input("Byte number: "))
    print(f"{proxi_list[byte]}")
    new_value = str(input("New hex value: "))
    proxi_list_new[byte] = new_value

    print(f"Previous proxi: {str(proxi)}")
    proxi_out = space.join(proxi_list_new)
    print(f"New proxi: {str(proxi_out)}")
    pyperclip.copy(str(set_proxi + proxi_out))

proxi_editor()