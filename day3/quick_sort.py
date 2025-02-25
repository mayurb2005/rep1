def partion_array(numbers, low, high):
    j = low
    pivot = numbers[high]
    for i in range(low, high):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i] 
            j += 1
    numbers[j], numbers[high] = numbers[high], numbers[j] 
    return j

def quick_sort(numbers, low, high):
    if low < high:
        pivot_index = partion_array(numbers, low, high)
        quick_sort(numbers, low, pivot_index-1)
        quick_sort(numbers, pivot_index+1, high)