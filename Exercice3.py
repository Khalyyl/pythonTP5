def text_to_index(txt):
    word_index = {}
    words = txt.split()

    for index, word in enumerate(words):
        if word not in word_index:
            word_index[word] = [index]
        else:
            word_index[word].append(index)

    return word_index

text = "ceci est un texte un exemple de texte"
result = text_to_index(text)
print(result)
