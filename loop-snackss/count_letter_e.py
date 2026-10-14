word = input("Enter a sentence: ")

count = 0

for letter in word:
    if letter == "e":
        count += 1

print("The letter e appears", count, "times.")