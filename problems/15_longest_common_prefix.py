str_arr = ["flower", "flow", "flight"]

def longest_commont_prefix(arr):
    prefix = ""
    for i in range(len(arr[0])):
        chars = arr[0][i]
        
        for word in arr:
            if i >= len(word) or word[i] != chars:
                return prefix
        
        prefix += chars
    return prefix

print(longest_commont_prefix(str_arr))