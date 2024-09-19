from string import ascii_uppercase

st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])

print([ascii_uppercase[i] for i in range(int(input()))])
