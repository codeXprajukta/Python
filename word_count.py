sentence = "Python is fun to learn"

word_count = 0
in_word = False

for char in sentence:
    if char != ' ' and not in_word:
        word_count += 1
        in_word = True
    elif char == ' ':
        in_word = False

print("Number of words:", word_count)
