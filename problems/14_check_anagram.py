s = "car"

t = "arcc"

# inputs = s , t

# output => True, False

def check_anagram(s, t):
    hash_map = {}
    hash_map2 = {}
    for value in s:
        hash_map[value] = hash_map.get(value, 0) + 1

    for value in t:
        hash_map2[value] = hash_map2.get(value, 0) + 1
    

    return hash_map2 == hash_map


print(check_anagram(s,t))