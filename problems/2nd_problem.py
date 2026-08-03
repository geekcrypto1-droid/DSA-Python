# write a function that returns an array of odd & even indexes of elements in an array


# Phase 1 find the output and inputs of you function and state the problem 

arr1 = {
    'test_arr' : [4, 12, 9, 21, 16, 17, 70, -1, 0],
    'input' : 'test_arr',
    'output' : {
        'odd_indexes' : [1,3,5,7],
        'even_indexes' : [0,2,4,6]
    }
}

# Phase 2: Edge cases


# 1 the array has 1 element
# 2 the array has 0 element
# 3 the elements are not sorted
# 4 0th index should be included in the even index or not


# Phase 3: write a solution in plain English

# 1 we create the function locate_indexes(test_arr)
# 2 we create 2 variables called odd_index = [] and even_index = []
# 3 we use for loop or while loop. If we use while loop we have to create a variable position/index
# 4 if we use for loop we have can use enumerate() function
# 5 if the index/position % 2 == 0 then we append the even list
# 6 if the index/position % 2 != 0 then we append the odd list
# lastly our function is going to return both the lists



# phase 3: Now write it in code
def locate_indexes(arr1):
    odd_index = []
    even_index = []
    for i, _ in enumerate(arr1):
        # print(i)
        if i % 2 == 0:
            even_index.append(i)
        else:
            odd_index.append(i)

    return odd_index, even_index

test_arr = [4, 12, 9, 21, 16, 17, 70, -1, 0]

print(locate_indexes(test_arr))


# 2nd Problem:  Modify the function to return values at odd/even indexes, not the indexes themselves.

# Phase 1 restate the problem: It says modify not create a new function. But the outputs should be different 

# expected output
# odd_values = [12, 21, 17, -1]
# even_values = [4, 9, 16, 70, 0]

# from here we can understand that most of the codes remain the same and we don't need to go through the edge cases so we can skip it

# Phase 3: Solution in plain English

# 1 we rename the vars in our function from index to value since it is not returning index anymore. To rename the function we can consult with the interviewer so far we will leave it as it is.
# 2 in our loop now that we want the values so we change back _ to j/values
# 3 now we append the j/value in our vars

# Phase 4: modify function

def locate_index_values(arr1):
    odd_values = []
    even_values = []
    for i, j in enumerate(arr1):
        # print(i)
        if i % 2 == 0:
            even_values.append(j)
        else:
            odd_values.append(j)

    return odd_values, even_values

test_arr2 = [4, 12, 9, 21, 16, 17, 70, -1, 0]

print(locate_index_values(test_arr))