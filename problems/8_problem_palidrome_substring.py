# x = 121

# print(x % 10)
# print(x // 10)
# # print(12 // 10)

def isPalindrome(value):
    x = value
    reversed_num = 0

    if value < 0:
        return False

    while x != 0:
        last_digit = x % 10
        remaining = x // 10
        x = remaining
        reversed_num = reversed_num * 10 + last_digit


    if reversed_num == value:
        return True
    else:
        return False

    # return reversed_num

# print(isPalindrome(-121))




print(-121 // 10)
print(-13 % 10)
print(-13 // 10)
print(-2 // 10)
print(-1 // 10)
# x = 121

# last_digit = x % 10
# remaining = x // 10
# reversed = last_digit * 10

# print(reversed)