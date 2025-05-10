# a program to find out whether a student has passed or failed 
# if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user

a = []

n = int(input("Enter the number of subjects: "))
for i in range(n):
    element = int(input(f"enter marks obtained in subject {i + 1}: ")) 
    a.append(element)

def calculateResult(a,n):
    total = 0
    for i in range(n):
        if a[i] < 33:
            print(f"You failed because your marks in subject {i + 1} are less than 33% ({a[i]}).")
            return
        else:
            total += a[i]
    finalResult = (100 * total) / (n * 100)  
    if finalResult >= 40:
        print(f"Congratulations, You passed with {finalResult:.2f}%")
    else:
        print(f"You failed because your total percentage is below 40% ({finalResult:.2f}%)")

calculateResult(a,n) 
