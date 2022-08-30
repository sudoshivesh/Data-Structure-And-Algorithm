mylist=input("Enter elements : ").split()
A=[int(i) for i in mylist]
print("Before Sorting ",A)
length=len(A)
for i in range(length-1):
  min=i
  for j in range(i+1,length):
    if A[min]>A[j]:
      min=j
  if i!=min:
    A[i],A[min]=A[min],A[i]
print("After sorting the list is : ",A)
#This code is contributed by me
