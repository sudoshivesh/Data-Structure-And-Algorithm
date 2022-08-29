mylist = input("Enter numbers separated by space: ").split()
A=[int(i) for i in mylist]
print("Before Sorting the list was : ")
print(A)
A.sort()
print("After Sorting the list is: ")
print(A)
length = len(A)
low = 0
high = length-1
value = int(input("Enter the Number to search : "))
loc = -1
while(low<=high):
    mid=(low + high)//2
    if value==A[mid]:
        loc=mid+1
        break
    elif value>A[mid]:
        low=mid+1
    elif value<A[mid]:
        high=mid-1
        low=0
if loc==-1:
    print(value,"not found.")
else:
    print(value,"found at",loc,"position and at index",(loc-1))
