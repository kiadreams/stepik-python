text = input()
while '[u-' in text:
    index = text.find('[u-')
    text = text[:index] + chr(int(text[index + 3: index + 7])) + text[index+8:]
print(text)
