import json

with open('idf.json', 'r') as f:
    idf = json.load(f)

from lyricsToBow import lyrics_to_bow

lyrics = input("Enter your Query: ")
print(lyrics)


query = lyrics_to_bow(lyrics)

IDF_values = []

for term in query:
	if term in idf.keys():
		IDF_values.append((idf[term],term))

IDF_values.sort(reverse=True)
# print(IDF_values)
Combo_L = []

from itertools import combinations 

for r in range(len(IDF_values),0,-1):
	combo_r = list(combinations(IDF_values, r))
	# print(combo_r)
	combo_r.sort(reverse = True)
	Combo_L.append(combo_r)

# print(Combo_L)

for l in Combo_L:
	print(l)
	print(end='\n\n')