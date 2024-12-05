alphabet = {
    'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '#', 'g': '6', 'h': '[-]',
    'i': '|', 'j': '_|', 'k': '|<', 'l': '1', 'm': r'[]\/[]', 'n': r'[]\[]', 'o': '0',
    'p': '|D', 'q': '(,)', 'r': '|z', 's': '$', 't': "']['", 'u': '|_|', 'v': r'\/',
    'w': r'\/\/', 'x': '}{', 'y': '`/', 'z': '2'
}

text = list(input("").lower())

newText = []

for i in text:
    if i in alphabet:
        newText.append(alphabet[i])
    else:
        newText.append(i)

print(''.join(newText))