from collections import Counter

'lsit comprehension'
n= [1,2,3,4]
square= [i**2 for i in n if i%2==0]
print(square)

'Dictionary comprehension'
dic = {z:ord(z) for z in "abz"}
print(dic)

# **Practice**
# 1. From a list of words, build a dict `{length: count}`.  
#    _Expected_: For `["a","bb","bb","ccc"]` → `{1:1, 2:2, 3:1}`.
words = ["a","bb","bb","ccc","ccc","dddddd"]

for word in words:
    print(word, len(word))
# length_count = { k: (cnt := sum(1 for w in words if len(w) == k)) for k in set(map(len, words))
# }
length_count = {k:(cnt:= sum(1 for w in words if len(w)==k)) for k in set(map(len, words))}
print(length_count)

print("Hello world")

# words = [ "a","bb","bb","ccc","ccc","dddddd"]
# lenght_counter = {}
# map = map(len, words)
# map_list = list(map)
# print(map_list)
# print(set(map_list))

# for word in words:
# 	lenght_counter[len(word)] = lenght_counter.get(len(word), 0) + 1

# print(lenght_counter)

# for word in words:
#     length = len(word)
#     if length in length_count:
#         length_count[length] += 1
#     else:
#         length_count[length] = 1
# print(length_count)   
# Compressed version using dictionary comprehension
# length_count = dict(Counter(map(len, words)))
# print(length_count)
# for word in words:
#     print(len(word), words.count(word))

# length_count = {len(words): words.count(words) for words in words}
        # length_count = {}
        # for word in words:
        #     length = len(word)
        #     if length in length_count:
        #         length_count[length] += 1



        #         else length_count[length] = 1

#         # print(length_count)
# length_countt = {}
# length_countt = {len(word): length_count.get(len(word), 0) + 1 for word in words}
# print(length_countt)
