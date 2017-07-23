# 23.07.2017
# Markov chain with words


import random


filename = "zombie.txt"
with open(filename, 'r') as myfile:
    data = myfile.read().replace('\n', '').split()


# order of the ngrams
order = 3
ngrams = {}


for i in range(len(data) - 1):
    gram = data[i]
    if not gram in ngrams:
        ngrams[gram] = []
    else:
        ngrams[gram].append(data[i + 1])

# print(ngrams)


def createText():
    choice = random.choice(list(ngrams))
    currentGram = choice
    result = [currentGram]

    for i in range(100):
        # if the coresponding list is empty break the loop
        if not ngrams[currentGram]:
            break
        nextWord = random.choice(ngrams[currentGram])
        result.append(nextWord)
        currentGram = result[-1]

    return " ".join(result)

print(createText())
