def count(input_string):
    vowels = "aeiou"
    vcount = 0
    ccount = 0

    for char in input_string.lower():
        if 'a' <= char <= 'z':  # Check if the character is an alphabet
            if char in vowels:
                vcount += 1
            else:
                ccount += 1

    print(f"Original string: {input_string}")
    print(f"Number of vowels: {vcount}")
    print(f"Number of consonants: {ccount}")

# Example usage:
my_string = "Hello World"
count(my_string)