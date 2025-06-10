#1.Right angled pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="") 
    print()

#2.Inverted Right-Angled Triangle Pattern
for i in range(6,1):
     for j in range(i):
         print("*" , end="")
     print()

#3.Square Star Pattern
for i in range(1,6):
    for j in range(6):
        print("*" , end="")
    print()

#4.Hollow square pattern 
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#5.Right-Angled Triangle with Numbers
print("Right-Angled Triangle with Numbers:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#6.Inverted Number Triangle
print("\nInverted Number Triangle:")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#7.Left-Aligned Number Triangle
print("\nLeft-Aligned Number Triangle:")
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

#8.Pyramid Star Pattern
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

#9.Diamond Pattern
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))
 
for i in range (rows - 1 ,0 ,  -1):
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

#11.Hollow Pyramid Pattern
rows = 5

for i in range(1, rows + 1):
    if i == rows:
        print("*" * (2 * rows - 1))
    else:
        print(" " * (rows - i), end="")
        print("*", end="")
        if i > 1:
            print(" " * (2 * i - 3), end="")
            print("*", end="")
        print()