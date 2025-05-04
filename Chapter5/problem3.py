#empty dictionary. Allow 4 friends to enter their favorite language as
#value and use key as their names. Assume that the names are unique
n = int(input("Enter the number of entries: "))
entries = [(input("Enter Friend's name: "), input("Enter language: ")) for _ in range(n)]
d = dict(entries)

print(d)