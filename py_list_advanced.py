# Part 2

# Task 1: Find out which students both submitted their assignments and attended the class.


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

did_both = []

for element in submitted:
    if element in attended:
        did_both.append(element)

        print(did_both)

