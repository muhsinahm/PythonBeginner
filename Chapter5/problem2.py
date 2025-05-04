# program to input eight numbers from the user and display all the unique numbers (once)
integer_list = list(map(int, input("Enter integers separated by space: ").split()))
print("list",integer_list)
b = list(set(integer_list))

print("Unique Number",b)
