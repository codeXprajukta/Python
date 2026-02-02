def replace_digits(s):
    result = ""

    for ch in s:
        # ASCII values for '0' to '9' are 48 to 57
        if 48 <= ord(ch) <= 57:
            result += "*"
        else:
            result += ch

    return result


# Example
text = "User123 has 4 apples"
print(replace_digits(text))
