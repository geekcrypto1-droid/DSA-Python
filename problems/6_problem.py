# from collections import defaultdict

# 2 sum

# test = {
#     "input" : {'arr': [1,2,5,2,7,3,6,8,2,11,5,0], 
#                "target" : 16},
#     "output" : [9,10]
# }



# def sum_two_num(arr, target) :
#     hash_map = {}
#     for index, value in enumerate(arr):
#         complement = target - value

#         if complement in hash_map:
#             return [hash_map[complement], index]
        
#         hash_map[value] = index
    


# test_arr = [3,2,4]

# print(sum_two_num(test_arr, 6))




test_array = [1,2,8,-1,3,6,9]
# target = 7

def hash_algo(arr, target):
    hash_arr = {}
    for index, value in enumerate(arr):
        complement = target - value

        if complement in hash_arr:
            return [hash_arr[complement], index]
        hash_arr[value] = index
        print(hash_arr)


print(hash_algo(test_array, 7))

