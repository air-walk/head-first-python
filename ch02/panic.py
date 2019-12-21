phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove('D')
plist.remove("'")
plist.insert(2, " ")
plist.insert(4, 'a')
plist.insert(5, 'p')

for i in range(6):
  plist.pop()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
