#https://github.com/maxbane/simplegoodturing/blob/master/sgt.py

from nltk import SimpleGoodTuringProbDist, FreqDist

fd = FreqDist({'a':1, 'b':1, 'c': 2, 'd': 3, 'e': 4, 'f': 4, 'g': 4, 'h': 5, 'i': 5, 'j': 6, 'k': 6, 'l': 6, 'm': 7, 'n': 7, 'o': 8, 'p': 9, 'q': 10})

p = SimpleGoodTuringProbDist(fd)
p.prob('a')
print(getattr(p))
