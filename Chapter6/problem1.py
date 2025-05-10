#program to find the greatest of four numbers entered by the user
listOfNumbers = list(map(int, input("Enter four numbers separated by space: ").split()))
print("Added List ", listOfNumbers)
def largestNumber(listOfNumbers, n):
    maximun = listOfNumbers[0]

    for i in range(1, n):
        if listOfNumbers[i] > maximun:
            maximun = listOfNumbers[i]

    return maximun

n = len(listOfNumbers)
maxNumber = largestNumber(listOfNumbers, n)
print("Largest Number: ", maxNumber)


