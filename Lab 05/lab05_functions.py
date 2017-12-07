def createWordList(filename):
    infile = open(filename, 'r')
    s = infile.read()
    L = s.split('\n')
    return L[:-1]
    


def canWeMakeIt(myWord,myLetters):
    lettersList = []
    for i in range(0, len(myLetters)):
        lettersList.append(myLetters[i])
    for i in range(0, len(myWord)):
        if myWord[i] in lettersList:
            lettersList.remove(myWord[i])
        else:
            return False
        
    return True
        

def getWordPoints(myWord,letterPoints):
    WordPoints = 0
    for i in range(0, len(myWord)):
        WordPoints += letterPoints[myWord[i]]
    return WordPoints


def scrabbleWords(myLetters):
    wordList = createWordList('wordlist.txt')
    myWords = []
    myWord = 'abc'
    for i in range(0, len(wordList)):
        myWord = wordList[i]
        if canWeMakeIt(myWord,myLetters) == True:
            myWords.append(myWord)

    letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1,\
                    'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
                    's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

    pointWordList = []
    for word in myWords:
        myWord = word
        pointValue = getWordPoints(myWord,letterPoints)
        pointWordList.append((pointValue, myWord))

    pointWordList.sort(reverse = True)

    file = open(myLetters + '.txt', 'w')
    for tuple in pointWordList:
        print('{:<{}}{}'.format(tuple[1], str(len(myLetters) + 4),tuple[0]))
        file.write('{:<{}}{}\n'.format(tuple[1], str(len(myLetters) + 4),tuple[0]))

    file.close()   
    
