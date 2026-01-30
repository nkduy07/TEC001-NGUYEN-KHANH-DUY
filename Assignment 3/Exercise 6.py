
while True:
    word = input("Enter a word: ")
    mid = len(word) // 2
    if len(word) % 2 == 1:
        print(word[mid])
    else:
        print(word[mid -1 : mid +1])
    if word == "":
        print ("Exit")
        break
