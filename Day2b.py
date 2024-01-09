import re

sampleInput = open("SampleInput/sample2.txt", "r").read().splitlines()
puzzleInput = open("PuzzleInput/puzzle2.txt", "r").readlines()

#Set data to sampleInput or puzzleInput
file = puzzleInput

lineValue = []

#parameters
red = 12
green = 13
blue = 14

answer = 0

#class

class Game:
    def __init__(self, line):
        self.gameNumber = int(line[0].split(' ')[1])
        self.hands = line[1].split(';')

#Loop through the data
for line in file:
    game = Game(line.split(':'))
    possible = True

    maxRed = []
    maxGreen = []
    maxBlue = []

    for hand in game.hands:
        cubesList = hand.split(',')
        for cubes in cubesList:
            cube = cubes.split(' ')
            if "red" in cube[2]:
                maxRed.append(int(cube[1]))
            elif "green" in cube[2]:
                maxGreen.append(int(cube[1]))
            elif "blue" in cube[2]:
                maxBlue.append(int(cube[1]))

    red = max(maxRed)
    green = max(maxGreen)
    blue = max(maxBlue)
    subAnswer = red*green*blue
    answer += subAnswer

    print(str(game.gameNumber) + ":" + str(possible))
    print(answer)

print(answer)