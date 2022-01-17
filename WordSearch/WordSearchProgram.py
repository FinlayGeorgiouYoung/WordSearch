"""
ex2.py
Created by Finlay Georgiou-Young on 12/12/2017
"""

import sys

wordsearch = []

switch1 = False

#Allows user to input the file containing the grid to be used
while switch1 == False:
    file = input("Please enter a file name: ")
    try:
        f = open(file, "r")
        switch1 = True
    #If it can't open the file an error message is shown and the user is able to input again
    except IOError as error:
        print("\nThe file failed to open. Please try another file")
        

#Gets rid of the new line on each line of the file and puts each line of the grid into a list
print()    
for line in f:
        line1 = line.replace("\n", "")
        wordsearch.append(line1)

#Displays the full grid
for line in wordsearch:
    print(line)

    
print()

words = []

switch2 = False

#Allows user to input the file containing the words to be searched in the grid
while switch2 == False:
    file2 = input("Please enter a file name of words to be searched: ")
    try:
        f2 = open(file2, "r")
        switch2 = True
    #If it can't open the file an error message is shown and allows the user to input again
    except IOError as error:
        print("\nThe file failed to open. Please try another file")


#Gets rid of the new line on each line of the file and puts each line/word into a list
print()    
for line in f2:
        line1 = line.replace("\n", "")
        words.append(line1)

#Prints each word in the list(the words to be found in the grid)
print("Words to be found: ")
for line in words:
    print(line)



    



Wordinfo = {}
Wordsnotfound = []

#This function searches a given grid for different given words. It searches the grid from left to right, right to left, top to bottom and bottom to top. It returns dictionary of words that have been found and where they are and a list of words that haven't been found
def search(word, grid):

    #Searches the grid from left to right by trying to locate the word in each line of the grid
    for line in grid:
        if line.find(word) > 0:
            row = grid.index(line) + 1
            col = line.find(word) + 1
            wordpos = (row, col, "left to right")
            Wordinfo.update({word: wordpos})

    #Searches the grid from right to left by reversing each line of the grid
    for line in grid:
        if line[::-1].find(word) > 0:
            row = grid.index(line) + 1 
            col = len(line) - line[::-1].find(word)
            wordpos = (row, col, "right to left")
            Wordinfo.update({word: wordpos})


    #Rotates grid 90 degrees
    #Splits up characters of each line of the wordsearch
    char = []
    for line in grid:
        char.append(list(line))
    #Changes the each line of letters that were in the rows to letters that were in the columns 
    Wordsearchrotate = list(zip(*char))
    #Join the letters from the columns into strings of a list
    rotated = []
    for line in Wordsearchrotate:
        rotated.append("".join(line))
    
    
    #Searches the gid from top to bottom (or the 90 degree rotated grid from left to right) by trying to locate the word in each line of the grid
    for line in rotated:
        if line.find(word) > 0:
            col = rotated.index(line) + 1
            row = line.find(word) + 1
            wordpos = (row, col, "top to bottom")
            Wordinfo.update({word: wordpos})

    #Searches the gid from bottom to top (or the 90 degree rotated grid from right to left) by trying to locate the word in each line of the grid
    for line in rotated:
        if line[::-1].find(word) > 0:
            col = rotated.index(line) + 1 
            row = len(line) - line[::-1].find(word)
            wordpos = (row, col, "bottom to top")
            Wordinfo.update({word: wordpos})
        
        



    #Adds the word to a list if it isn't found in the grid
    if word not in Wordinfo:
        Wordsnotfound.append(word)
                


            

#Goes through the wordsearch function and searches for the words given as a file
print()
for line in words:
    search(line, wordsearch)

#Sorts the words found into alphabetical order
Wordinfo2 = sorted(Wordinfo)

#Prints what words have been found and where
for word in Wordinfo2:
    values = Wordinfo[word]
    print(word, "found:", ((values)[2]), "from row", ((values)[0]), "col", ((values)[1]))


#Prints the words not found in alphabetical order
print("\nWords not found: ")
for word in sorted(Wordsnotfound):
    print(word)




quitting = input("\nIf you would like to quit enter Yes: ")

if quitting == "Yes".upper() or "Yes".lower() or "Yes".title():
    sys.exit
















