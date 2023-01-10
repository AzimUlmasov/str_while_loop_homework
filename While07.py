def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer

    """
    idx = 0
    count = 0
    while idx < len(s):
        if s[idx].isdigit() and int(s[idx])%2==0:
            count += 1
        idx += 1 
    return count
print(main('56786543250'))