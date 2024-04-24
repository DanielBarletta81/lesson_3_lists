# Task 1: Sort in descending order and display sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse= True)

print(grades)

# Task 2: Calculate the average grade and display it.

average = int(sum(grades) / len(grades))

print(average)


# Task 3:  Replace any grade below 80 with the value Failed.

grades[7:10] = ["Failed", "Failed, Failed "]

print(grades)