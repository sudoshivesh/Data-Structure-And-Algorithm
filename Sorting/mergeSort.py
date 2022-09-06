def merge(A,p,mid,r):
    L=A[p:mid+1]
    R=A[mid+:r+1]
    L.append(1000) #Sentinal Element
    R.append(1000) #Sentinal Element
    i=j=0
    for k in range(p,r+1):
        if L[i]<R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
def mergesort(A,p,r):
    if p<r:
        mid=(p+r)//2  #divide
        mergesort(A,p,mid)
        mergesort(A,mid+1,r)
        merge(A,p,mid,r)
mylist=input("Enter Element : ").split()
A=[int(I) for i in mylist]
length=len(A)
print("Before Sorting : ",A)
mergesort(A,0,length-1)
print("Sorted List : ",A)
