# author: Michał Rybiński
# nickname: rybinskm
# date of create: 21-03-2021

import crcmod.predefined
import binascii

hex_entry_value = binascii.a2b_hex('2348765fd834782938aebbc93485023947')
print(f'{hex_entry_value}')
calc_method = crcmod.predefined.mkCrcFun('kermit')
calc_result = calc_method(hex_entry_value)
print(f'{calc_result}')
