

import math
import ast


fileName = input("Name of original file (end it with .txt): ")
f = open(fileName, "r")
inputStr = f.read()
fps1, score1 = inputStr.split('\n')
fps1 = ast.literal_eval(fps1)
score1 = ast.literal_eval(score1)

print("Length of first record in seconds: " + str(score1[-1][1] / fps1))



fileName = input("Name of file to add  (end it with .txt): ")
f = open(fileName, "r")
inputStr = f.read()
fps2, score2 = inputStr.split('\n')
fps2 = ast.literal_eval(fps2)
score2 = ast.literal_eval(score2)


delay = float(input("Delay in seconds from start of the original file: "))

def addToArray(array, numToAdd):
    for i in range(len(array)):
        array[i][1] = int(array[i][1] + numToAdd)
    return

def multInArray(array, numToMult):
    for i in range(len(array)):
        array[i][1] = int(array[i][1] * numToMult)
    return

lcm = math.lcm(fps1, fps2)
mult1 = lcm / fps1
mult2 = lcm / fps2

multInArray(score1, mult1)
multInArray(score2, mult2)

print(score1)
print(score2)

addToArray(score2, int(lcm * delay))

print(score2)


fullScore = list()
numOfNotes = len(score1) + len(score2)
ix1 = 0
ix2 = 0
for i in range(numOfNotes):

    if (ix1 == len(score1)):
        fullScore.append(score2[ix2])
        ix2 += 1
        continue

    if(ix2 == len(score2)):
        fullScore.append(score1[ix1])
        ix1 += 1
        continue

    if(score1[ix1][1] <= score2[ix2][1]):
        fullScore.append(score1[ix1])
        ix1 += 1
    else:
        fullScore.append(score2[ix2])
        ix2 += 1
        
# print(fullScore)

nameOfEndFile = str(input("Name of end file: "))
outputStr = str(lcm) + "\n" + str(fullScore)
fileName = nameOfEndFile + ".txt"
f = open(fileName, mode="x")
f.write(outputStr)
f.close()




