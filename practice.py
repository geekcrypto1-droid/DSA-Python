nums = [1,2,3,4]


def solution(nums):
    n = len(nums)
    result = [1] * n
    product = 1
    for i in range(n):
        result[i] = product
        product *= nums[i]

    product = 1
    for i in range(n-1, -1, -1):
        result[i] *= product
        product *= nums[i]

    return result

    
    

print(solution(nums))