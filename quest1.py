from xml.dom.minidom import ProcessingInstruction
# 1. Given `s = "abracadabra"`, print a dict of letter -> count.
#    _Expected_: `{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}` (order may vary).

# tryin to seperate
s = "abracadabra"
non_repeat = "".join(sorted(set(s)))
print(non_repeat)

# tryin to sepearte
loop = ""
for char in s:
    if char not in loop:
        loop += char
print(loop)

# ------------main Solution----------
dict = {}

for char in s:
    dict[char] = dict.get(char, 0) + 1
    print(dict[char])
    print(dict)
print(dict)