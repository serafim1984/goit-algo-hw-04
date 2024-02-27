import random
import timeit

prefilled_list_10 = [random.randint(1, 10) for _ in range(10)]

prefilled_list_100 = [random.randint(1, 100) for _ in range(100)]

#Merge sort functions

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Insertion sort functions

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]
insertion_sort(numbers)



#print(merge_sort(prefilled_list_10))
#print(merge_sort(prefilled_list_100))

print('\n Execution time for 10 items array \n')

execution_time_merge_10 = timeit.timeit(lambda: merge_sort(prefilled_list_10), number=1)

print(f"Execution time merge 10: {execution_time_merge_10} seconds")

execution_time_insertion_10 = timeit.timeit(lambda: merge_sort(prefilled_list_10), number=1)

print(f"Execution time insertion 10: {execution_time_insertion_10} seconds")

execution_time_sort_10 = timeit.timeit(prefilled_list_10.sort, number=1)

print(f"Execution time sort 10: {execution_time_sort_10} seconds")

execution_time_sorted_10 = timeit.timeit(lambda: sorted(prefilled_list_10), number=1)

print(f"Execution time sorted 10: {execution_time_sorted_10} seconds")

print('\n Execution time for 100 items array \n')

execution_time_merge_100 = timeit.timeit(lambda: merge_sort(prefilled_list_100), number=1)

print(f"Execution time merge 100: {execution_time_merge_100} seconds")

execution_time_insertion_100 = timeit.timeit(lambda: merge_sort(prefilled_list_100), number=1)

print(f"Execution time insertion 100: {execution_time_insertion_100} seconds")

execution_time_sort_100 = timeit.timeit(prefilled_list_100.sort, number=1)

print(f"Execution time sort 100: {execution_time_sort_100} seconds")

execution_time_sorted_100 = timeit.timeit(lambda: sorted(prefilled_list_100), number=1)

print(f"Execution time sorted 100: {execution_time_sorted_100} seconds")

print('\n Results of time measurement shows that method sort and function sorted() works considerably faster especially with longer arrays')