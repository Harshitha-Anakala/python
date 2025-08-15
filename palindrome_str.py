a = input( )
def is_palindrome(a):
    if a == a[::-1]: 
        return "Palindrome"
    else:
        return "Not Palindrome"
print(is_palindrome(a))
