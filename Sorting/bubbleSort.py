def bubbleSort(A):
	for i in range(length):                  #Outerloop will be executed till last element
		for j in range(0,length-i-1) :       #Last one is sorted hence loop will reduced to one 
			if A[j] > A[j+1]:                #Swap if element found greater than neighboring element
				A[j],A[j+1]=[A[j+1],A[j]
				
mylist=input("Enter elements : ").split()
A=[int(i) for i in mylist]
length = len(A)
print("Before Sorting : ",A)
bubbleSort(A)
print("After Sorting : ",A)
