def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:        
                left.append(x)
            else:
                right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)

input_file = 'input_quick_sort.txt'

with open(input_file, 'r+') as file:
    numbers = [int(line.strip()) for line in file.readlines()]
    sorted_numbers = quick_sort(numbers)
    file.seek(0)
    file.truncate()
    file.writelines([str(number) + '\n' for number in sorted_numbers])
