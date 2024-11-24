l =[]
lt =[]
a = int(input("Enter no. of vertical lines:"))
b = int(input("Enter no. of horizontal lines:"))
for i in range(0,a):
    l.append([])
    for j in range(0,b):
        print("enter element of",i+1,"line",j+1,"element",end="")
        c = input(":")
        l[i].append(c)

for i in range(0,b):
    lt.append([])

for j in range(0,len(l)):
    for i in range(0,b):
        lt[i].append(l[j][i])


print("original matrix")
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j],end=" ")
    print()
print("transepose matrix")
for i in range(0,len(lt)):
    for j in range(0,len(lt[i])):
        print(lt[i][j],end=" ")
    print()
