def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    swapped =  False
    for j in range(n-i-1):
      if arr[l]>arr[j+1]:
        arr[l],arr[l+1] = arr[l+1], arr[l]
        swapped =  True
     if swapped == False:
       return
example_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(example_list)
print("Sorted list:", sorted_list)




# Bubble sort
# It always compares with the adjacent element.
# It has a time complexity O(n**2)
# Bubble sort is a stable algorithm. This means if there are same values in the list or array, their order will remain the same as the original order.
