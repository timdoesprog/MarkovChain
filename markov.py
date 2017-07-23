# 23.07.2017
# Markov chain


import random


filename = "exampleText.txt"
with open(filename, 'r') as myfile:
    data = myfile.read().replace('\n', '')


# order of the ngrams
order = 3
ngrams = {}


for i in range(len(data) - order - 1):
    gram = data[i:i + order]
    if not gram in ngrams:
        ngrams[gram] = []
    else:
        ngrams[gram].append(data[i + order])

# print(ngrams)


def createText():
    choice = random.randint(0, len(data) - order)
    currentGram = data[choice:choice + order]
    result = currentGram

    for i in range(100):
        # if the coresponding list is empty break the loop
        if not ngrams[currentGram]:
            break
        nextLetter = random.choice(ngrams[currentGram])
        result += nextLetter
        currentGram = result[-order:]

    return result

print(createText())
