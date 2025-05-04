#program to sum a list with 4 numbers
a = []

n = int(input("Enter the number of students: "))
for i in range(n):
    element = int(input(f"Enter marks obtained by student {i + 1}: "))
    a.append(element)

print("Sum of Marks", sum(a))

