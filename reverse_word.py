def reverse_words(s):
    words = []
    word = ""

    # Extract words manually
    for ch in s:
        if ch != ' ':
            word += ch
        else:
            words.append(word)
            word = ""
    words.append(word)  # add last word

    # Build reversed string manually
    result = ""
    i = len(words) - 1
    while i >= 0:
        result += words[i]
        if i != 0:
            result += " "
        i -= 1

    return result


# Example usage
s = "hello world python"
print(reverse_words(s))
