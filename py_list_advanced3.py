# Task 3: Remove names of students from "attended" that didn't submit the assignment

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for element in attended:
    if element not in submitted:
        attended.remove(element)

        print(attended)