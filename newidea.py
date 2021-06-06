import numpy
import sys

# print(sys.argv[1])
# s = sys.argv[1]
# s = s.lower()
def analys(s):
    res = []
    letters = dict()
    for ch in range(97,123):
        letters[chr(ch)] = 0
    for l in s:
        if l in letters:
            letters[l]+=1

    maxE = max(letters.values())
    size = maxE + 1


    grafRes = numpy.zeros(shape=[27,maxE+2])
    for ch in range(97, 123):
        graf = []
        graf.append(chr(ch))
        graf.append('|')
        for ii in range(letters[chr(ch)]):
            graf.append('*')
        for jj in range(maxE-letters[chr(ch)]):
            graf.append(' ')
        grafRes = numpy.vstack([grafRes, graf])
    print(grafRes[27:])


# analys(s)
print()
print()
print()
for i in range(5):
    print("     *     *     ")
print()
print("     *     *      ")
print("      *   *       ")
print("       ***        ")