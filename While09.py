def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    count = 0
    while idx < len(s):
        if s[idx].isdigit():
            count += int(s[idx]) 
        idx += 1 
    return count
print(main('987654'))