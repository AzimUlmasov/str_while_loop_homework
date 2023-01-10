def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    count = 0
    while idx < len(s):
        if s[idx].isdigit() and int(s[idx])%2==1:
            count += int(s[idx]) 
        idx += 1 
    return count
print(main('589765'))