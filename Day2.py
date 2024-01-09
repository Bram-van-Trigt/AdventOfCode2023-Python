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
for  line in file:
    game = Game(line.split(':'))
    possible = True

    for hand in game.hands:
        cubesList = hand.split(',')
        for cubes in cubesList:
            cube = cubes.split(' ')
            if "red" in cube[2]:
                if int(cube[1]) > red:
                    possible = False
            elif "green" in cube[2]:
                if int(cube[1]) > green:
                    possible = False
            elif "blue" in cube[2]:
                if int(cube[1]) > blue:
                    possible = False

    if possible == True:
        answer += game.gameNumber

    print(str(game.gameNumber) + ":" + str(possible))
    print(answer)

print(answer)