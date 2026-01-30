phrase = input("Enter a word: ")
words = phrase.split()
c = [word[0].upper() for word in words]
result = ''.join(c)
print(result)

