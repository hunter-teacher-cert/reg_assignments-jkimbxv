#homework solutions
#1: which sort is better? pros and cons
#pros of bubble sort: not much memory needed, n^2 cost
#pros of sselection sort: easy to implement. cons: n^2

#2: larger data sets?
#larger data sets would mean sorts take longer because of the n^2 Algorithms
#the sorts may not be efficient enough.

dataset = [10, 18, 6, 9, 16, 11, 3, 2, 15, 19, 1, 20, 14, 8, 12, 17, 5, 7, 13, 4];

#easy: looks for a max instead of minimum
def findmax(arr,start,end):
    max = start #max index
    while (start < end):
        if (arr[start]>arr[max]):
            max = start
        start+=1
    return max
print(findmax(dataset,0,len(dataset)))

#medium: selection sort: sorts greatest to least
def selectionsort(arr):
    i = 0
    while (i < len(dataset)):
        currmax = findmax(arr,0,len(dataset)-i)
        arr.append(arr[currmax])
        arr.pop(currmax);
        i+=1
    return arr
print(selectionsort(dataset.copy()))

#spicy: bubble sort: implement a sinking sort instead.
def swap(arr,a,b):
    newarr = arr#.copy()
    temp = newarr[a]
    newarr[a] = newarr[b]
    newarr[b] = temp
    return newarr

def sinkingsort(arr):
    newarr = arr.copy()
    j=0
    while (j<len(newarr)):
        i = len(newarr)-1
        while (i>0):
            if (newarr[i]<newarr[i-1]):
                swap(newarr,i,i-1)
            i-=1
        j+=1
    return newarr

print(sinkingsort(dataset))
