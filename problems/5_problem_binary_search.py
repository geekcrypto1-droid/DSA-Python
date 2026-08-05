# # from jovian.pythondsa import evaluate_test_cases

# # given a list of sorted array, find the most effective method to find the index of a given number in that
# #  array in the least possible iteration

# # 1: 
# test = {'input' : [9,8,7,6,5,4,3,2,1,0],
#         'query' : 0,
#         'output' : 11
#         }

# input = [9,8,7,6,5,4,3,2,1,0]

# # 2 : edge cases
# # 1 the query is at the start of the arr
# # 2 query is at the end of the arr, or the start of the arr
# # 3 query is not in the arr
# # 4 array contains negative valeus
# # 5 array has only one element
# # 6 arrat is empty


# # 3 Code in plain English

# # we will use binary search as it is the most effective method for a sorted array
# # 1 first we check the middle of our arr
# # 2 if the element is greater than the query then we discard all the elements on the right
# # 3 if it is shorter then we discard the left elements 
# # 4 we again check the middle element and repeat these steps until we find the query

# def binary_search(arr, query):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         middle_number = arr[mid]

#         if middle_number == query:
#             return mid
#         elif middle_number > query:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1
# print(binary_search(input, 0))


# # Given a sorted array (ascending) and a target number,
# # return the first and last index of that number.

# # If not found → return [-1, -1].

# test = {
# 'input' : [1,1,2,2,2,4,5],
# 'target' : 2,
# 'Output': [1, 3]
# }

# # 1 the array has negative values
# # 2 the array has 0 values
# # 3 the array has only 1 value
# # 4 the target only appears once


# # 3 Plain English
# # 1 we first find where the target first appeared
# # 2: we find where the target last appeard 
# # 3: we save both their indexes in a var and return it

# # 'input' : [1,2,2,2,3,4,5],

# def locate_firs_and_last(arr, target):
#     def find_last():
#         first, last = 0, len(arr) -1
#         result = -1
#         while first <= last:
#             mid = (first + last) // 2
#             if arr[mid] == target:
#                 result = mid
#                 first = mid + 1
#             elif arr[mid] > target:
#                 last = mid -1
#             elif arr[mid] < target:
#                 first = mid + 1
#         return result
    
#     def find_first() :
#         first, last = 0, len(arr) -1
#         result = -1
#         while first <= last:
#             mid = (first + last) // 2
#             if arr[mid] == target:
#                 result = mid
#                 last = mid - 1
#             elif arr[mid] < target:
#                 first = mid + 1
#             elif arr[mid] > target:
#                 mid + 1
#         return result
    
#     return [find_first(), find_last()]


# print(locate_firs_and_last(test['input'], 2))
# # evaluate_test_cases(locate_firs_and_last, test)









# Given a sorted array (ascending) and a target number,
# return the first and last index of that number.



# test_array = {
#     'input' : [1,2,3,4,5,6,7,8,9],
#     'target' : 8,
#     'output' : 7 
# }



# test_arr = [1,2,3,4,5,6,7,8]

# def find_target(arr, target):
#     low = 0
#     high = len(arr) -1

#     while low <= high:
#         mid = (low + high) // 2
#         if target < arr[mid]:
#             high = mid - 1
#         elif target > arr[mid]:
#             low = mid + 1
#         else:
#             return mid
#     return -1
        


# print(find_target(test_arr, 8))








# locate the first and last appearance of a target in a sorted array
# using binary search

test_arr = {
    'input' : [1,2,2,2,3,3,3,5,5,5],
    'target' : 2,
    'output' : [1,3]
}


arr = [1,2,2,2,3,3,3,5,5,5]

def find_first_and_last(arr, target): 
    def find_first():
        first = 0
        last = len(arr) - 1
        result = -1
        while first <= last:
            mid = (first + last) // 2

            if target == arr[mid]:
                result = mid
                last = mid - 1
            elif target > arr[mid]:
                first = mid + 1
            elif target < arr[mid]:
                last = mid - 1
        return result
    def find_last():
        first = 0
        last = len(arr) - 1
        while first <= last:
            result = -1
            mid = (first + last) // 2

            if target == arr[mid]:
                result = mid
                first = mid + 1
            elif target > arr[mid]:
                first = mid + 1
            elif target < arr[mid]:
                last = mid - 1
        return result
    return [find_first(), find_last()]
    

print(find_first_and_last(arr, 2))