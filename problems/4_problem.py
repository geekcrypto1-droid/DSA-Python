# Write a function that returns the Second Highest element in an array


test_arr = [1, 21, -2, -3, 42, 52, 7 , 52, 9, 0, 42]

test = {
    "input" : test_arr,
    "output" : 42
}
# 2
# All the elements in the array is negative
# the array has one element
# it has no element
# it has only 2 element
# it has only 1  element
# it is not sorted
# the array has multiple same values which are second highest

# 3

# 1 we first check if our array.len > 2 else we return none
# 2 we are not gonna sort the array because that way our time complexity will be O(N log N)
# 3 we will create 2 var called highest and second_highest and both are equal to the first index of our array since our first edge case is all negative
# 4 we will use the standard for loop and iterate just once and our time complexity will O(N) || better
# 5 we will compare the elements if they are greater than our highest var
# 6 if yes: we will assign the second_highest the value of highest
# 7 and we change the highest with the greater value of the arr
# 8 when the loop ends we return the second highest


# 4

def locate_second_highest(test):
    if not test or len(test) < 2:
        return None
    highest = second_highest = test[0]
    for i in test:
        if i > highest:
            second_highest = highest
            highest = i
    return second_highest

print(locate_second_highest(test["input"]))