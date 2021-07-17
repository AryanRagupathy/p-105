import csv
import statistics

with open("data.csv", newline = '') as f:
    read_data = csv.reader(f)
    file_data = list(read_data)

data = file_data[0]


def get_mean(numbers):
    number_of_elements = len(numbers)
    total_value = 0
    
    for i in numbers:
        total_value = total_value + int(i)
    
    mean = total_value / number_of_elements
    return mean


squares = []
for number in data:
    x = int(number) - get_mean(data)
    x = x ** 2
    squares.append(x)


sum_of_numbers = 0
for element in squares:
    sum_of_numbers = sum_of_numbers + element


result = sum_of_numbers / (len(data) - 1)


standard_deviation =result**(1/2)
print("The standard deviation of the data manually:             ", standard_deviation)


#I Found This Out 

data = [60, 61, 65, 63, 98, 99, 90, 95, 91, 96]
print("The standard deviation of the data through a function:   ", statistics.stdev(data))