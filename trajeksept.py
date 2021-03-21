tsr_list = []

try:
    print(tsr_list[0])
except IndexError:
    tsr_list = [0x00]

print(tsr_list[0])
