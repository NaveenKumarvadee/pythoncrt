a.pattern
x=int(input())
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print("\n")
b.
x=int(input())
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
c.
x=int(input())
for i in range(x):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")
d.pyramid pattern
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*  ",end=" ")
    print("\n")
E.diamond pattern
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*  ",end=" ")
    print("\n")
for i in range(x-2,-1,-1):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*  ",end=" ")
    print("\n")
F.odd sequence
x=int(input())
for i in range(x+4):
    for j in range(x-i+4):
        print(" ",end=" ")
    for j in range(i+1):
        if(i%2!=0):
            break
        else:
           print("*  ",end=" ")
    print()
g.hollow square
n=int(input())
for i in range(n):
    for j in range(n):
       if i==0 or j==0 or i==n-1 or j==n-1:
          print("*",end=" ")
       else:
          print(" ",end=" ")
    print()
H.hollow rightangle triangle
n=int(input())
for i in range(n):
    for j in range(i+1):
       if i==n-1 or j==0 or i ==j:
          print("*",end=" ")
       else:
          print(" ",end=" ")
    print()

