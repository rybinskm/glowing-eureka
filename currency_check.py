import matplotlib.pyplot as plt

values = []
dates = []

""" rewrite values from text file """
currency_value_file = open(r'C:\Users\Rybston\Desktop\currency.txt', 'r')
for line in currency_value_file:
    # print(line)
    value = line.split('-')[0]
    # print(value)
    date = line.split('-')[1].strip()
    # print(date)
    values.append(float(value))
    dates.append(date)

lowest_value = min(values)
highest_value = max(values)

""" finding dates for proper min/max values """
for i in range(len(values)):
    if values[i] == lowest_value:
        lowest_value_date = dates[i]
    elif values[i] == highest_value:
        highest_value_date = dates[i]

print(f'Lowest value: {lowest_value} ({lowest_value_date})')
print(f'Highest value: {highest_value} ({highest_value_date})')

""" drawing plot part """
plt.ylabel('Worth')
plt.xlabel('Dates')
plt.plot(values, marker='o')  # marking all values on the graph
plt.axhline(y=highest_value, color='r', linestyle='--', label=f'Highest value: {highest_value} ({highest_value_date})')
plt.axhline(y=lowest_value, color='b', linestyle='--', label=f'Lowest value: {lowest_value} ({lowest_value_date})')
plt.plot(dates, values)  # creating plot for proper lists
plt.legend(bbox_to_anchor=(1.0, 1), loc='upper center')  # set legend on the graph
plt.show()
