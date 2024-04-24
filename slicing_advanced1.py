# Task 1: Extract the temperatures for the second week (7 days) of the month.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_slice = temperatures[7:14]

print(second_week_slice)

# Task 2: Extract values above 100

above_hundred = temperatures[24:]

print(above_hundred)

#Task 3: Reverse order of list, and extract 5th-10th day temps.

temperatures.reverse()

print(temperatures)

fifth_to_tenth_day = temperatures[4:10]

print(fifth_to_tenth_day)