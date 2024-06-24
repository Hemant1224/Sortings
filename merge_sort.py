def merge(arr, low, mid, high):
    # Create temporary arrays for left and right halves
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    # Initialize pointers for left (i), right (j), and merged array (key)
    i = j = 0
    key = low
    
    # Merge the temporary arrays back into arr[low...high]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[key] = left[i]
            key += 1
            i += 1
        else:
            arr[key] = right[j]
            key += 1
            j += 1

    # Copy the remaining elements of left[], if any
    while i < len(left):
        arr[key] = left[i]
        key += 1
        i += 1

    # Copy the remaining elements of right[], if any
    while j < len(right):
        arr[key] = right[j]
        key += 1
        j += 1

def mergeSort(arr, l, r):
    # Only proceed if there are elements to sort
    if l < r:
        # Find the middle point to divide the array into two halves
        m = (l + r) // 2
        
        # Call mergeSort on the first half
        mergeSort(arr, l, m)
        
        # Call mergeSort on the second half
        mergeSort(arr, m + 1, r)
        
        # Merge the two halves sorted in the previous steps
        merge(arr, l, m, r)

# Example usage:
arr = [10, 5, 30, 15, 7]
# Call mergeSort on the entire array
mergeSort(arr, 0, len(arr) - 1)
# Print the sorted array
print(*arr)  # Output: 5 7 10 15 30
