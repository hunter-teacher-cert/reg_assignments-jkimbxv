#bubble sort

def bubblesort(arr):
    a = 0
    while (a<len(arr)):
        i = 0
        while (i<len(arr)-1-a):
            if (arr[i+1]<arr[i]):
                swap(arr,i+1,i)
            i+=1
        a+=1
    return arr

def swap(arr,a,b):
    newarr = arr#.copy()
    temp = newarr[a]
    newarr[a] = newarr[b]
    newarr[b] = temp
    return newarr

dataset = [10, 18, 6, 9, 16, 11, 3, 2, 15, 19, 1, 20, 14, 8, 12, 17, 5, 7, 13, 4];

print(bubblesort(dataset))
