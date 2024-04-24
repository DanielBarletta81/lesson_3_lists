# Task 1: Filter out students who have grades below 80. 
# Print the name, grade and activity. Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


students_approved = []

for i in range(len(grades)):
    if grades[i] < 80:
        print(f"{students[i]}, {grades[i]}, {activities[i]}")
    else:
        students_approved.append(students[i])

# Task 2: For the remaining students, 
#add students name in a new list named students_approved.





# Task 3: Print the list students_approved

print(students_approved)