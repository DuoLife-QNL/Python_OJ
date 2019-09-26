word_num = int(input())
dict = {}

x = 1
while x <= word_num:
    cat_word, dog_word = map(str, input().split())
    dict[dog_word] = cat_word
    x += 1

doc = []
word = input()
while True:
    if word == "dog":
        break
    else:
        if word in dict.keys():
            doc.append(dict[word])
        else:
            doc.append("dog")
        word = input()

for x in doc:
    print(x)