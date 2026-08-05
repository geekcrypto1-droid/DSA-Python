test_arr = {
    'input' : [1,2,2,2,3,3,3,3,4,4,4,4],
    'target' : 2,
    'output'  : [1,3]
}

def locate_first_and_last(arr, target):
    def locate_first():
        first, last = 0, len(arr) - 1
        result = -1
        while first <= last:
            mid = (first + last) // 2
            middle_number = arr[mid]

            if target == middle_number:
                result = mid
                last = mid - 1
            elif target > middle_number:
                first = mid + 1
            elif target < middle_number:
                last = mid - 1

        return result
    
    def locate_last():
        first, last = 0, len(arr) - 1
        result = -1
        while first <= last:
            mid =(first + last) // 2
            middle_number = arr[mid]
            
            if target == middle_number:
                result = mid
                first = mid + 1
            
            elif target > middle_number:
                first = mid + 1

            elif target < middle_number:
                last = mid - 1
        return result
    
    return [locate_first(), locate_last()]
    


print(locate_first_and_last(test_arr['input'], test_arr['target']))




# target not in array
print(locate_first_and_last([1,2,2,2,3], 7))   # expected [-1, -1]

# target appears once
print(locate_first_and_last([1,2,2,2,3], 3))   # expected [4, 4]

# empty array
print(locate_first_and_last([], 2))             # expected [-1, -1]