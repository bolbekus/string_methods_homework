def main(s):
    """
    A str containing the letter "a" is given. Find the number of letters "a" in this variable.
    Args:
        s: str
    Returns:
        int: answer
    """
    
    return s.count('a',1,15)

print(main("Mobile development"))