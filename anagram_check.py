def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    # Count characters in first string
    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    # Subtract counts using second string
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True


# Example
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False



