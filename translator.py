def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            translation += 'g'
        else:
            translation += letter
    return translation


print(translate(input('Enter a word: ')))
