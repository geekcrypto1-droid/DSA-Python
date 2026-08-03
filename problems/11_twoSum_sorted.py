input_arr = [2,7,11,15, 20]

target = 9

output = [1,2]

def sumArray(arr, target):
    if len(arr) <= 1:
        return
    
    left = 0
    right = len(arr) - 1
    while left < right:
        total_sum = arr[left] + arr[right]
        
        if total_sum == target:
            return [left + 1, right + 1]
        elif total_sum < target:
            left += 1
        elif total_sum > target:
            right = right - 1


         
    


print(sumArray(input_arr, target))

