def single_rot_words(rot_words, *other_words):
    same_words = []
    for word in other_words:
        if word.lower() in rot_words.lower() or rot_words.lower() in word.lower():
            same_words.append(word)
    return same_words
result1 = single_rot_words('rich', 'richiest orichalcum', 'cheers', 'richies')
result2 = single_rot_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

