import random
import math
import cTurtle
import hist

def coinFlipTrial(M, N):
    x = 0
    for i in range (1, N+1):
        if random.randint(1,2) == 1:
            x += 1

    if x >= M:
        return True
    else:
        return False



def coinFlipExperiment(M, N, nTrials):
    successCount = 0
    for i in range (1, nTrials+1):
        if coinFlipTrial(M, N) == True:
            successCount += 1

    return successCount/nTrials



def randomWalkFirstPassageTrial(D):
    x = 0
    y = 0
    steps = 0
    while math.sqrt(x**2 + y**2) < D:
        theta = random.uniform(0,2*math.pi)
        x += math.cos(theta)
        y += math.sin(theta)
        steps += 1
        
    return steps


def monteCarloRandomWalkFirstPassage(D, nTrials):
    y = []
    for i in range(1, nTrials+1):
        y.append(randomWalkFirstPassageTrial(D))

    hist.plotHistogram(y, nBins = 55)
    print(sum(y)/nTrials)


def randomUniformSum(M):
    y = 0
    for i in range (1, M+1):
        x = random.uniform(0,1)
        y += x
    return y

def plotRandomUniformSum(M, N, nBins):
    lst = []
    for i in range (1, N+1):
        lst.append(randomUniformSum(M))

    hist.plotHistogram(lst, binMin=0, binMax=M, nBins = nBins)




        
        
    



    
    
        
        
