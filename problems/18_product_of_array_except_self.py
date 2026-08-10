# prefix and suffix algorithm
inputs = [1, 2, 3, 4]
output = [24, 12, 8, 6]

# print(output * inputs)

def solution(arr):
    prefix = []
    suffix = []
    product = 1  # start with 1 (neutral for multiplication)

    for value in arr:
        prefix.append(product)  # append BEFORE multiplying
        product *= value         # update running product

    # print(prefix)  # [1, 1, 2, 6] ✅


    suffix_product = 1
    for value in reversed(arr):
        suffix.insert(0, suffix_product)
        suffix_product *= value


    # print(suffix)


    result = []
    for i in range(len(arr)):
        result.append(prefix[i] * suffix[i])


    # return [prefix[i] * suffix[i] for i in range(len(arr))]

    return result

print(solution(inputs))