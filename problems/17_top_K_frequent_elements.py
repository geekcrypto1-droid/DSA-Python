# Input: 
nums = [1,1,1,2,2,2,2,3]
k = 2

# Output: [1,2]  ← the 2 most frequent elements

# Input: nums = [1], k = 1
# Output: [1]


def solution(arr, k):
    hash_map = {}
    counter = 0

    for value in arr:
        hash_map[value] = hash_map.get(value, 0) + 1

    hash_map = sorted(hash_map, key= lambda x: hash_map[x], reverse=True)
        

    return hash_map[:k]




print(solution(nums, k))