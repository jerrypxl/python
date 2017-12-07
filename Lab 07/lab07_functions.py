class Sentence:
    def __init__(self, s):
        self.s = s
        self.L = self.s.split()
        self.punctuation = self.s[-1]

    def getSentence(self):
        return self.s

    def getWords(self):
        L = []
        L = self.s.split()
        L[-1] = L[-1][0:-1]
        return L

    def nChars(self):
        return len(self.s)

    def __len__(self):
        return len(self.s.split())

    def __getitem__(self, idx):
        return self.s.split()[idx]

    def __setitem__(self, idx, word):
        self.s.split()[idx] = word
        self.L[idx] = word
        self.s = ' '.join(self.L)

    def averageWordLength(self):
        x = 0
        L = []
        L = self.s.split()
        L[-1] = L[-1][0:-1]
        for i in range(0, len(L)):
            x += len(L[i])
        return x/len(L)

    def minWordLength(self):
        x = 0
        lst = []
        L = []
        L = self.s.split()
        L[-1] = L[-1][0:-1]
        for i in range(0, len(L)):
            x = len(L[i])
            lst.append(x)
        lst.sort()
        return lst[0]

    def maxWordLength(self):
        x = 0
        lst = []
        L = []
        L = self.s.split()
        L[-1] = L[-1][0:-1]
        for i in range(0, len(L)):
            x = len(L[i])
            lst.append(x)
        lst.sort()
        return lst[-1]

    def getPunctuation(self):
        return self.punctuation

    def setPunctuation(self, p):
        newSelf = self.s[0:-1]
        self.s = newSelf + p
        self.punctuation = p

    def capitalize(self):
        lst = []
        L = []
        L = self.s.split()
        L[-1] = L[-1][0:-1]
        for i in range(0, len(L)):
            self.L[i] = L[i].capitalize()
        self.s = ' '.join(self.L) + self.punctuation

    def __add__(self, s2):
        L = self.s.split()
        L[-1] = L[-1][0:-1]
        string = ' '.join(L)
        for i in range(0, len(s2)):
            letter = s2[0]
            newLetter = letter.lower()
        s2 = s2[1:]
        newS2 = newLetter + s2
        newString = string + ', '
        return (newString + newS2)

    def __str__(self):
        print(self.s)
        
        
        
            
        
        
