num = int(input("Enter the number of rows: ")) # this input function will require a user to input a value
# we want to print an * in ascending order. every time it increases, it will form an new line
for x in range(0, num): # this for loop function sets a value ranging from 0 up to but excluding num for x
    for i in range(0, x+1): #this for loop function is sets a value ranging 0 up to but excluding x+1 for i
        print("*", end=" ") # for every value of i, it will print an *. the end="" is so that its printed to the side
    print() # this print() is so that every loop will print a new line

print("\n") # this print function is only to create a line space between each line
# this, like the previous shape however, we print out blank spaces, then print out the * in ascending order
for x in range(0, num): # this for loop function sets a value ranging from 0 up to but excluding num for x
    for i in range(0, num - x ): #this for loop function is sets a value ranging 0 up to but excluding x+1 for i
        print(" ", end=" ") #with this for loop, it will print out a space for i times to the side
    for z in range(0, x+1): # this for loop function set a value ranging 0 up to but excluding x+1 for z
        print("*", end=" ") # so this print * for z times to the side, after the space has been printed
    print() # this print function is only to create a line space between each line

print("\n")
# for this shape, basically just print it upside down. * in descending order, with every decrease, we print out a new line
for x in range(0, num): # this for loop function sets a value ranging from 0 up to but excluding num for x
    for i in range(0, num - x): #this for loop function sets a value ranging from 0 up to but excluding num-x
        print("*", end=" ")# so * will be printed for num - x times to the side.
    print() # this print function is only to create a line space between each line

print("\n")
# this shape is very similar to the second one, we print out spaces first but then * in descending order
for x in range(0, num): # this for loop function sets a value ranging from 0 up to but excluding num for x
    for i in range(0, x):
        print(" ", end=" ") #print out the space to the side for i times
    for z in range(0, num - x):
        print("*", end=" ") #this will print * to the side for num -x times
    print()

print("\n")
# making a pyramid. printing * in ascending order
for x in range(0, num):
    for i in range(0, num - x):
        print(end=" ")
    for z in range(0, x+1):
        print("*", end=" ") #this print * to the side for x+1 times
    print("\r")

print("\n")
#this section is the same as making the top pyramid
for x in range(0, num):
    for i in range(0, num-x-1):
        print(end=" ")
    for z in range(0, x+1):
        print("*", end=" ")
    print()
#hhere, we make an inverted pyramid, by switching the parameters of the 2 nested for loops
for x in range(0, num):
    for i in range(0, x + 1):
        print(end=" ")
    for z in range(0, num- x - 1):
        print("*", end=" ")
    print()
