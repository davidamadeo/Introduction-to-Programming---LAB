num = int(input("Enter the number of rows: "))
for x in range(0, num):
    for i in range(0, x+1):
        print("*", end=" ")
    print()

print("\n")

for x in range(0, num):
    for i in range(0, num - x ):
        print(" ", end=" ")
    for z in range(0, x+1):
        print("*", end=" ")
    print()

print("\n")

for x in range(0, num):
    for i in range(0, num - x):
        print("*", end=" ")
    print()

print("\n")

for x in range(0, num):
    for i in range(0, x):
        print(" ", end=" ")
    for z in range(0, num - x):
        print("*", end=" ")
    print()

print("\n")

for x in range(0, num):
    for i in range(0, num - x -1):
        print(end=" ")
    for z in range(0, x+1):
        print("*", end=" ")
    print("\r")

print("\n")

for x in range(0, num):
    for i in range(0, num-x-1):
        print(end=" ")
    for z in range(0, x+1):
        print("*", end=" ")
    print()
for x in range(0, num):
    for i in range(0, x + 1):
        print(end=" ")
    for z in range(0, num-x -1):
        print("*", end=" ")
    print()
