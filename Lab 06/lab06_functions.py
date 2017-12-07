def createCityPopDict():
    D={}
    x=open('pop3.txt','r')
    y=x.readlines()
    x.close()
    for eachline in y:
        L=eachline.split()
        key=' '.join(L[1:-1])
        D[key]=int(L[-1])
    return D

def createCityLatLonDict():
    D={}
    z=open('latLon3.txt','r')
    y=z.readlines()
    z.close()
    for eachline in y:
        L=eachline.split()
        key=' '.join(L[2:])
        value=(float(L[0]),-float(L[1]))
        D[key]=value
    return D

def createStateColorDict():
    D={}
    file=open('stateAdj.txt','r')
    k=file.read()       
    file.close()
    H=k.split('\n')
    L1=[]
    L2=[]
    for x in H[::2]:
        if x:
            L1.append(x.split(',')[0])
    for y in H[1::2]:
        if y:
            L2.append(int(y))
    for z in range(len(L1)):
        abbr=L1[z].lower()
        num=L2[z]
        D[abbr]=num
    return D



def drawLower48Map():
    stateColorDict=createStateColorDict()
    cityLatLonDict=createCityLatLonDict()
    cityPopDict=createCityPopDict()

    colorList=['cyan','purple','deep pink','gold']

    latlist=[v[0] for v in cityLatLonDict.values()]
    lonlist=[v[1] for v in cityLatLonDict.values()]

    import turtle;
    import math;
    peter=turtle.Turtle('turtle')
    s=turtle.Screen()
    X=max(lonlist)-min(lonlist)
    Y=max(latlist)-min(latlist)
    s.setworldcoordinates(min(lonlist)-.1*X, min(latlist)-.1*Y, max(lonlist)+.1*X,max(latlist)+.1*Y)

    peter.speed(0)
    string=''
    file=open('output.txt','w')
    peter.ht()
    file.write('{:30}{:15}{:15}{:15}{:15}{:15}\n'.format('City Name:','Latitude:','Longitude:','Population:','Dot Size:','Color:'))
    for City in cityLatLonDict.keys():
        latlon=cityLatLonDict[City]
        if City in cityPopDict:
            population=cityPopDict[City]
            dotSize=4+math.ceil((population/50000)**(1/2))
            peter.dot(dotSize)
        else:
            peter.dot(4)
        peter.up()
        peter.setposition(latlon[1],latlon[0])
        peter.down()
        stateColorDict=createStateColorDict()
        abbr=City.split(',')[-1].lower()
        color1=stateColorDict[abbr]
        color2=colorList[color1]
        peter.pencolor(color2)

        if City in cityPopDict:
            population=cityPopDict[City]
            dotSize=4+math.ceil((population/50000)**(1/2))
            file.write('{:30}{:15}{:15}{:15}{:15}{:15}\n'.format(City,str(latlon[0]), str(-latlon[1]), str(population), str(dotSize), color2))
        else:
            dotSize=4
            population=''
            file.write('{:30}{:15}{:15}{:15}{:15}{:15}\n'.format(City, str(latlon[0]), str(-latlon[1]), str(population), str(dotSize),color2))
    file.close()

drawLower48Map()

