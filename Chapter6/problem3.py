#a program to find whether a given username contains less than 10
#characters or not
username = input("Enter username: ")
if(len(username)<10):
    print("username has less than 10 characters")
else:
    print("username has more than 10 characters")