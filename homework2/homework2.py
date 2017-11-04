print("Vvedite suda 1 word pls:")
word = input()
for i in range(0, len(word), 2):
	if word[i] == 'о' or word[i] == 'п' or word[i] == 'е':
		print(word[i])
