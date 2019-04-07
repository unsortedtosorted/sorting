"""
  if an element is smaller than its prev, keep doing pairwise swaps
  

"""


def insertionSort(arr):

    if len(arr) <= 1:
        return arr


    for i in range(1,len(arr)):

        j = i

        while j > 0 and arr[j] < arr[j-1]:

            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp

            j-=1

arr1 = [5, 2, 4, 6, 1, 3]
insertionSort(arr1)
print (arr1)
