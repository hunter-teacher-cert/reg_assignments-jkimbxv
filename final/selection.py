#selection sort
def selectionsort(arr):
    i = 0
    while (i < len(arr)):
        currmin = findmin(arr,0,len(arr)-i)
        arr.append(arr[currmin])
        arr.pop(currmin);
        print(arr)
        i+=1
    return arr

#findmax finds the first index smallest number in the array starting from start
def findmin(arr,start,end):
    imin = start;
    i = start+1
    while (i < end):
        if (arr[i]<arr[imin]):
            imin = i
        i+=1
    return imin

dataset = [10, 18, 6, 9, 16, 11, 3, 2, 15, 19, 1, 20, 14, 8, 12, 17, 5, 7, 13, 4];


print(selectionsort(dataset))

#medium assignment
#code a selectionSort2 that will return a sorted array from greatest to least!
#you may need to code a findmax first...
