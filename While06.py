def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    vowels = 'aeiou'
    a, x = 0, 0
    while a < len(s):
        if not s[a].lower() in vowels and s[a].isalpha():
            x += 1
        a += 1 
    return x
print(main('CodeschoolUz'))