# create a function that finds the lowest and highest value of an array


#  1: Function => highest and lowest value. as the interviewer. Should it return seperately or return in another array?

test_arr = [0, 8, 21, -1, 6, 12, 2]

# we will assume we need to return both values in an array
# so the output will be 

myfunct = {
    'input' : [0, 8, 21, -1, 6, 12, 2],
    'output' : [21, -1]
}


# 2: Edge Cases are
# array has one element 
# array has no element 
# array is not sorted
# array is sorted
# array has negative values
# array has 2 or more same highest or lowest vlaue


# point: WE need to ask the interviewer if our function should return all the same high or low values in case there are multiple same values

# 3: Solution in plain english 

# by now I can only come up with 2 solutions
# 1st is for loop
# 2nd is sort the array and return the last and first index

# we will go with first

# first we create a function
# we create 2 empty vars or array called high_value and low_value. We can ask the interviewer for a var name if we cannot come up with one
# we run a loop that iterates through each elements in array
# upon each iteration we check if the element is greater or lower than our var values
# if yes, we assign them to our vars
# if no, we move on to the next until we reach the end of our array

# 4: solution in Code:

def find_high_low_elements(arr):
    if not arr:
        return None
    high_value = low_value = arr[0]
    for i in arr:
        if i > high_value:
            high_value = i
        if i < low_value:
            low_value = i
    return [high_value, low_value]



print(find_high_low_elements(myfunct['input']))