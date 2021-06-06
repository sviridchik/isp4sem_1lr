import sys

import numpy

# print(sys.argv[1])
if len(sys.argv)<2:
    #print("ENTER PLEASE STRING")
    s = None
else:
    s = sys.argv[1]
    s = s.lower()


def analys(s):
    if s is None:
        print("ENTER PLEASE STRING")
        return
    res = []
    letters = dict()
    for ch in range(97, 123):
        letters[chr(ch)] = 0
    for l in s:
        if l in letters:
            letters[l] += 1

    maxE = max(letters.values())
    size = maxE + 1

    grafRes = numpy.zeros(shape=[27, maxE + 2])
    for ch in range(97, 123):
        graf = []
        graf.append(chr(ch))
        graf.append('|')
        for ii in range(letters[chr(ch)]):
            graf.append('*')
        for jj in range(maxE - letters[chr(ch)]):
            graf.append(' ')
        grafRes = numpy.vstack([grafRes, graf])


    for row in range(27, 53):
        out = ""
        for elem in grafRes[row]:
            out += " "
            out += elem
        print(out)


analys(s)
print()
print()
print()
for i in range(3):
    print("      *   *     ")
print()
print("     *     *      ")
print("      *   *       ")
print("       ***        ")
