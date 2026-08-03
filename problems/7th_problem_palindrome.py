x= "radar"
def isPalindrome(x):
    reverse = ""
    for char in x:
        reverse = char + reverse
    if reverse == x:
        return True
    else:
        return False



print(isPalindrome(x))

print('a' + 'r') 
print('d' + 'ar')
print('a' + 'dar')