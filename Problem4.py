#returns largest palindrome number made by 2 3 digit numbers
Number1 = 999
Limit = 100


def PalindromeCheck(number):
    return number == number[::-1]

def GreatestPalindrome():
    GCPalindrome = 0
    for i in range(Number1, Limit, -1):
        for j in range(i, Limit, -1):
            if PalindromeCheck(str(i*j)):
                if i*j > GCPalindrome:
                    GCPalindrome = i*j
    return GCPalindrome

print GreatestPalindrome()

