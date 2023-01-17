# from https://realpython.com/python-refactoring/

# Compares x to y and prints relationship
x = 5; y = int(input("Enter a number:"))
equality = "is equal to" if x == y else "is less than" if x < y else "is more than"
print(str(x) + ' ' + equality  + ' ' + str(y))
