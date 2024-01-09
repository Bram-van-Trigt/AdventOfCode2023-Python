import re

sampleInput = open('SampleInput/sample3.txt' , 'r' ).read().splitlines()
puzzleInput = open('PuzzleInput/puzzle3.txt' , 'r' ).readlines()

#Set data to sampleInput or puzzleInput
file = puzzleInput

lineValue = []

#parameters
answer = 0
checkList = ['!' , '@' , '#' , '$' , '%' , '&' , '^' , '*' , '=' , '+' , '-' , '/' , ';' ]

fileArray = []
#Loop through the data
for  line in file:
    fileArray.append(line)

for lineNr in range(len(fileArray)):
    valid = False
    partNr = ' ' 

    for charNr in range(len(fileArray[lineNr])):
        if fileArray[lineNr][charNr].isnumeric() is True:
            partNr = partNr + fileArray[lineNr][charNr]

            if lineNr == 0:
                if charNr == 0:
                    #check current line 
                    test = fileArray[lineNr][charNr+1]
                    if any (char in test for char in checkList) == True:
                        valid = True
                    #check line below
                    if any (char in fileArray[lineNr+1][charNr:charNr+2] for char in checkList) == True:
                        valid = True

                elif charNr == len(fileArray[lineNr])-1:
                    #check current line 
                    if any (char in fileArray[lineNr][charNr-1] for char in checkList) == True:
                        valid = True
                    #check line below
                    if any (char in fileArray[lineNr+1][charNr-1:charNr+1] for char in checkList) == True:
                        valid = True
                else:
                    #check current line 
                    if any (char in fileArray[lineNr][charNr-1:charNr+2] for char in checkList) == True:
                        valid = True
                    #check line below
                    if any (char in fileArray[lineNr+1][charNr-1:charNr+2] for char in checkList) == True:
                        valid = True

            elif lineNr == len(fileArray)-1:
                if charNr == 0:
                    #check line above
                    if any (char in fileArray[lineNr-1][charNr:charNr+2] for char in checkList) == True:
                        valid = True
                    #check current line 
                    if any (char in fileArray[lineNr][charNr+1] for char in checkList) == True:
                        valid = True

                elif charNr == len(fileArray[lineNr]):
                    #check line above
                    if any (char in fileArray[lineNr-1][charNr-1:charNr+1] for char in checkList) == True:
                        valid = True
                    #check current line 
                    if any (char in fileArray[lineNr][charNr-1] for char in checkList) == True:
                        valid = True
                else:
                    #check line above
                    if any (char in fileArray[lineNr-1][charNr-1:charNr+2] for char in checkList) == True:
                        valid = True
                    #check current line 
                    if any (char in fileArray[lineNr][charNr-1:charNr+2] for char in checkList) == True:
                        valid = True

            else:    
                if charNr == 0:
                    #check line above
                    if any (char in fileArray[lineNr-1][charNr:charNr+2] for char in checkList) == True:
                        valid = True
                    #check current line 
                    if any (char in fileArray[lineNr][charNr+1] for char in checkList)  == True:
                        valid = True
                    #check line below
                    if any (char in fileArray[lineNr+1][charNr:charNr+2] for char in checkList) == True:
                        valid = True

                elif charNr == len(fileArray[lineNr]):
                    #check line above
                    if any (char in fileArray[lineNr-1][charNr-1:charNr+1] for char in checkList) == True:
                        valid = True
                    #check current line 
                    if any (char in fileArray[lineNr][charNr-1] for char in checkList) == True:
                        valid = True
                    #check line below
                    if any (char in fileArray[lineNr+1][charNr-1:charNr+1] for char in checkList) == True:
                        valid = True
                else:
                    #check line above
                    if any (char in fileArray[lineNr-1][charNr-1:charNr+2] for char in checkList):
                        valid = True
                    #check current line 
                    if any (char in fileArray[lineNr][charNr-1:charNr+2] for char in checkList):
                        valid = True
                    #check line below
                    if any (char in fileArray[lineNr+1][charNr-1:charNr+2] for char in checkList):
                        valid = True
        elif valid is True:
            answer += int(partNr)
            #Reset variables for next partnumber
            valid = False
            print(partNr)
            partNr = '' 
        else:
            partNr = '' 

print(answer)    