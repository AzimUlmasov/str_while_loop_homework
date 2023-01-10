def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    count = 0
    while idx < len(s):
        if s[idx].isupper():
            count += 1
        idx += 1 
    return count
print(main('CodeschoolUz'))