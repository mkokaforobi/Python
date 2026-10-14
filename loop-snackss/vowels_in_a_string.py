word = input("Enter a sentence: ")

count = 0

for letter in word:
    if letter.lower() in "aeiou":
        count += 1
