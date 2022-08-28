# author:               Michał Rybiński
# nickname:             rybinskm
# date of create:       12-08-2022
# date of last edit:    12-08-2022
# example training functions

import matplotlib.pyplot as plt
import random
from decorators_training import time_execution


@time_execution
def prime_checker(number):
    checked_divider_list = []
    divider_list = []
    divisor_counter = 0

    for divider in range(1, int(number+1)):
        if number % divider == 0:
            divisor_counter += 1
            divider_list.append(divider)
        checked_divider_list.append(divider)

    if divisor_counter == 2:
        print(f'{number} is a prime number.')
    else:
        print(f'{number} is not a prime number.')
        print(f'Is is divisible by: {divider_list}')

    # matplot part
    plt.xlabel(f'Dividers of {number}')
    plt.xticks(divider_list)
    plt.ylabel('Checked numbers')
    plt.yticks(checked_divider_list)
    plt.show()


def mail_generator(address):
    if '@' in address:
        print('Address email is correct.')
        name_part = address.split('@')[0]
        name_part_2 = '@' + address.split('@')[1]
        number = random.randint(1000, 9999)
        new_address = name_part + str(number) + name_part_2
        print(f'New generated mail: {new_address}')
    else:
        print('Missing @ sign.')


def palindrom_check(word):
    if word == word[::-1]:
        print(f'Word "{word}" is a palindrom.')
    else:
        print(f'Word "{word}" is not a palindrom.')


unordered_list = [3, 6, 4, 0, 7, 9]


def list_sort(unordered_list):
    print(f'Unordered list: {unordered_list}')
    ordered_list = sorted(unordered_list)
    print(f'Ordered list: {ordered_list}')

