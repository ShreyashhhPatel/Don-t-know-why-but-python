words = [ "a","bb","bb","ccc","ccc","dddddd"]
lenght_counter = {}
map = map(len, words)
map_list = list(map)
print(map_list)
print(set(map_list))

for word in words:
	lenght_counter[len(word)] = lenght_counter.get(len(word), 0) + 1

print(lenght_counter)
