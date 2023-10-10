while True:
    input_str = input("Please enter two words separated by a space (or 'done' to exit): ")
    if input_str.lower() == 'done':
        break
    words = input_str.split()
    if len(words) == 0:
        break
    elif len(words) == 1:
        print("Only one word entered:", words[0])
    elif len(words) == 2:
        word1, word2 = words[0], words[1]
        if word1 < word2:
            print("The word that comes before in lexicographical order is:", word1)
        elif word2 < word1:
            print("The word that comes before in lexicographical order is:", word2)
        else:
            print("Both words are the same:", word1)
    else:
        print("Invalid input. Please enter two words separated by a space.")
print("Bye!")
