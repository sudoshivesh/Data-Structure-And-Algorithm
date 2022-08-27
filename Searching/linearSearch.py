mylist = input("Enter numbers seperated by space : ").split()
A = [int(i) for i in mylist]
print("The Given List is : ")
print(A)
length = len(A)
value = int(input("Enter a number to search : "))
loc = -1
for i in range(length):
    if value == A[i]:
        loc = i+1
        break
if loc == -1:
    print(value,"not found")
else:
    print(value,"found at",loc,"position and at index :",(loc-1))
