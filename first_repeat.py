def find_first_repeating(s):
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return char
        seen_chars.add(char)
    return None

# Example usage:
print(find_first_repeating("programming"))
print(find_first_repeating("abcdef"))
print(find_first_repeating("hello"))