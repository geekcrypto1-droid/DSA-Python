Input = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def group_anagrams(strs):
    hash_map = {}
    for word in strs:
        key = "".join(sorted(word))

        if key not in hash_map:
            hash_map[key] = []

        hash_map[key].append(word)
        
    return list(hash_map.values())

    


print(group_anagrams(Input))