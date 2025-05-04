# program to accept marks of 6 students and display them in a sorted manner
a = []

n = int(input("Enter the number of students: "))
for i in range(n):
    element = input(f"enter marks obtained by students {i + 1}: ")
    a.append(element)

print("Unsorted", a)
a.sort()
print("Sorted",a)
