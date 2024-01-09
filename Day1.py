import re

sampleInput = open("SampleInput/sample1.txt", "r").read().splitlines()
puzzleInput = open("PuzzleInput/puzzle1.txt", "r").readlines()


#Set data to sampleInput or puzzleInput
file = puzzleInput


lineValue = []

#Loop through the data
for  line in file:
    
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three" )
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    
    numbers = re.findall(r'\d+', line)
    
    if( len(numbers[0]) < 2 ):
        firstDigit = numbers[0]
    else:
        firstDigit = numbers[0][0]

    if( len(numbers[-1]) < 2 ):
        lastDigit = numbers[-1]
    else:
        lastDigit = numbers[-1][-1]

    twoDigit = int(firstDigit + lastDigit)

    lineValue.append(twoDigit)


answer = 0

for number in lineValue:
    answer += number
    print(answer)

print(" the first answer is " + str(answer))




# puzzleAnswer = 0
# matches = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# for line in file:
#     numberIndexes =  [(i, c) for i, c in enumerate(line) if c.isdigit()]
#     print(numberIndexes)

#     #check for first digit
#     startLine = line[0:numberIndexes[0][0]]
#     if any(x in startLine for x in matches):
#         for n in range( 0, len(startLine)-1, 1 ):
#             checkLine = startLine[n:n+5]
#             if "one" in checkLine:
#                 firstDigit = "1"
#                 break
#             elif "two" in checkLine:
#                 firstDigit = "2"
#                 break 
#             elif "three" in checkLine:
#                 firstDigit = "3"
#                 break 
#             elif "four" in checkLine:
#                 firstDigit = "4"
#                 break
#             elif "five" in checkLine:
#                 firstDigit = "5"
#                 break
#             elif "six" in checkLine: 
#                 firstDigit = "6"
#                 break
#             elif "seven" in checkLine:
#                 firstDigit = "7"
#                 break
#             elif "eight" in checkLine:
#                 firstDigit = "8"
#                 break
#             elif "nine" in checkLine:
#                 firstDigit = "9"
#                 break
#     else:
#         firstDigit = numberIndexes[0][1]

#     #check for second digit
#     endLine = line[numberIndexes[-1][0]:-1]
#     if any(x in endLine for x in matches):
        
#         for n in range(len(endLine)-1, -1, -1 ):
#             checkLine = endLine[n:n-5]
#             if "one" in checkLine:
#                 secondDigit = "1"
#                 break
#             elif "two" in checkLine:
#                 secondDigit = "2"
#                 break
#             elif "three" in checkLine:
#                 secondDigit = "3"
#                 break
#             elif "four" in checkLine:
#                 secondDigit = "4"
#                 break
#             elif "five" in checkLine:
#                 secondDigit = "5"
#                 break
#             elif "six" in checkLine: 
#                 secondDigit = "6"
#                 break
#             elif "seven" in checkLine:
#                 secondDigit = "7"
#                 break
#             elif "eight" in checkLine:
#                 secondDigit = "8"
#                 break
#             elif "nine" in checkLine:
#                 secondDigit = "9"
#                 break
#     else:
#         secondDigit = numberIndexes[-1][1]

#     #combine digits
#     digit = int(firstDigit + secondDigit)
#     # print(digit)
#     puzzleAnswer += digit

# print(puzzleAnswer)
