import numpy
import math




testInitPattern = [

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

size_matrice = 33
pixelStart = (0, 28)

res_tmp = []


def testAlgo():
    solution_user = doExercice(testInitPattern, 2)



def trouverPixelAvecLePlusDePixelAdjacent(pixelCercle, centreCercle, segment, d):

    listPixelAdjMax = ((None,None),[])

    for pixel in pixelCercle:


        listPixelAdj = (pixel, trouverPixelAdjacent(pixel, segment))


        if len(listPixelAdj[1]) > len(listPixelAdjMax[1]):
            listPixelAdjMax = listPixelAdj


    #on prend le 1er pixel
    bestPixelListe = listPixelAdjMax[1]
    maxPixel = None
    maxDistance = 0

    if len(bestPixelListe) == 0:
        for pixel in pixelCercle:
            testInitPattern[pixel[1]][pixel[0]] = 6

    for pixel in bestPixelListe:
        currentPixelValue = calculDistanceNewSegment(pixel, centreCercle)

        if abs(d-currentPixelValue[1]) < abs(d-maxDistance):
            maxDistance = currentPixelValue[1]
            maxPixel = currentPixelValue[0]


    return maxPixel



def trouverPixelAvecLePlusDePixelAdjacentCercle(pixelsCercle, centreCercle, listePixelCercle, d):

    listPixelAdjMax = ((None,None),[])


    for pixel in pixelsCercle:
        listPixelAdj = (pixel, trouverPixelAdjacentCercle(pixel, listePixelCercle))

        if len(listPixelAdj[1]) > len(listPixelAdjMax[1]) and testInitPattern[pixel[1]][pixel[0]] !=2:
            listPixelAdjMax = listPixelAdj

    #on prend le 1er pixel
    bestPixelListe = listPixelAdjMax[1]
    maxPixel = None
    maxDistance = 0


    if len(bestPixelListe) == 0:
        for pixel in pixelsCercle:
            testInitPattern[pixel[1]][pixel[0]] = 6

    for pixel in bestPixelListe:
        currentPixelValue = calculDistanceNewSegment(pixel, centreCercle)

        if abs(d-currentPixelValue[1]) < abs(d-maxDistance):
            maxDistance = currentPixelValue[1]
            maxPixel = currentPixelValue[0]


    return maxPixel





def trouverPixelAdjacentCercle(pixel, listePixelCercle):
    x = pixel[0]
    y = pixel[1]


    listPixel = []

    if x <= size_matrice - 1 and y <= size_matrice - 1 and x >= 0 and y >= 0:

                if (x + 1, y) in listePixelCercle:
                    listPixel.append((x + 1, y))

                if (x-1,y) in listePixelCercle:
                    listPixel.append((x - 1, y))

                if (x, y - 1) in listePixelCercle:
                    listPixel.append((x, y - 1))

                if (x, y + 1) in listePixelCercle:
                    listPixel.append((x, y + 1))



    return listPixel




def calculDistanceNewSegment(pixel, finalPixel):

    x0 = pixel[0]
    y0 = pixel[1]

    x1 = finalPixel[0]
    y1 = finalPixel[1]


    xd = abs(x1 - x0)
    yd = abs(y1 - y0)

    d = math.sqrt(xd*xd+yd*yd)
    return (pixel,d)


def trouverPixelAdjacent(pixel, segment):
    x = pixel[0]
    y = pixel[1]
   # print("x" + str(x))
  #  print("y" + str(y))

    listPixel = []

    if x <= size_matrice - 1 and y <= size_matrice - 1 and x >= 0 and y >= 0:

                if (x + 1, y) in segment:
                    listPixel.append((x + 1, y))

                if (x + 1, y + 1) in segment:
                    listPixel.append((x + 1, y + 1))

                if (x + 1, y - 1) in segment:
                    listPixel.append((x + 1, y - 1))

                if (x-1,y) in segment:
                    listPixel.append((x - 1, y))

                if (x - 1, y - 1) in segment:
                    listPixel.append((x - 1, y - 1))

                if (x - 1, y + 1) in segment:
                    listPixel.append((x - 1, y + 1))

                if (x, y - 1) in segment:
                    listPixel.append((x, y - 1))

                if (x, y + 1) in segment:
                    listPixel.append((x, y + 1))

#    print("listPixel")
#    print(listPixel)

    return listPixel




def resetMatrice(currentKosh):

    for linge in currentKosh:

        for pixel in linge:

            testInitPattern[pixel[1]][pixel[0]] = 0





def traceKosh(finalKosh):
    for segment in finalKosh:
        for pixel in segment:
            testInitPattern [pixel[1]][pixel[0]] = 1



def doExercice(InitPattern, koshValue):

    koshSegments = []
    kosh0 = initKosh0(pixelStart)
    koshSegments.append(kosh0)

    traceKosh(koshSegments)

    finalKosh = koshCreator(koshValue, 1, koshSegments)



    for ligne in testInitPattern:
        print(ligne)

    for pixel in res_tmp:
        testInitPattern[pixel[1]][pixel[0]]=7

    print(res_tmp)

    return finalKosh






def initKosh0(pixelStart):

    listPixelInitKosh0 = []

    id = 0
    y = pixelStart[1]

    while id < size_matrice:
        listPixelInitKosh0.append((id, y))
        id += 1

    return listPixelInitKosh0



def calculDistance(koshValue):
    return size_matrice / (3**(koshValue))



def splitSegment(segment, d):

    startPixelCentre = segment[0]
    endPixelCentre = segment[len(segment)-1]

    startCercle = testCercle(d, startPixelCentre)
    endCercle = testCercle(d, endPixelCentre)



    middlePixelStartCercle = None
    middlePixelEndCercle = None



    for pixel in startCercle:
        if pixel in segment:
            middlePixelStartCercle = pixel

    for pixel in endCercle:
        if pixel in segment:
            middlePixelEndCercle = pixel


    if middlePixelStartCercle == None:
        middlePixelStartCercle = trouverPixelAvecLePlusDePixelAdjacent(startCercle, startPixelCentre, segment, d)

    if middlePixelEndCercle == None:
        middlePixelEndCercle = trouverPixelAvecLePlusDePixelAdjacent(endCercle, endPixelCentre, segment, d)


    middleStartCercle = testCercle(d, middlePixelStartCercle)
    middleEndCercle = testCercle(d, middlePixelEndCercle)




    pixelIntersection = None

    for pixel in middleStartCercle:
        if pixel[0] < 33 and pixel[0] > 0 and pixel[1] < 33 and pixel[1] > 0 :
            if pixel in middleEndCercle and testInitPattern[pixel[1]][pixel[0]] !=2:
                pixelIntersection = pixel

    print("BISOIR")

    if pixelIntersection == None:
        print("BIJOUR")
        pixelIntersection = trouverPixelAvecLePlusDePixelAdjacentCercle(middleStartCercle ,startPixelCentre , middleEndCercle, d)


 #   for pixel in middleStartCercle:

   #     if pixel[0] < 33 and pixel[0] > 0 and pixel[1] < 33 and pixel[1] > 0:
        #    testInitPattern[pixel[1]][pixel[0]] = 3

  #  for pixel in middleEndCercle:
     #   if pixel[0] < 33 and pixel[0] > 0 and pixel[1] < 33 and pixel[1] > 0:
       #     testInitPattern[pixel[1]][pixel[0]] = 4


  #  for ligne in testInitPattern:
      #  print(ligne)


    #closeAngle = (720,(-1, -1))
    #print("closeAngle")


   # for pixelEnd in middleStartCercle:

   #     currentAngle = calculAngle(middlePixelEndCercle, middlePixelStartCercle, pixelEnd)



    #    if abs(60 - currentAngle) < abs(60 - closeAngle[0]) and \
       #         pixelEnd[0] < 33 and\
     #           pixelEnd [0] > 0 and \
      #          pixelEnd[1] < 33 and\
       #         pixelEnd [1] > 0 and \
       #         testInitPattern[pixelEnd[1]][pixelEnd[0]] != 2:


        #    closeAngle = (currentAngle,pixelEnd)
          #  print(closeAngle)


  #  closePixel = findPixelWithBestAngle(d*d, closeAngle[1], middlePixelStartCercle)

   # print(closeAngle)



    newListSegment = []

    newListSegment.append(getLine(startPixelCentre[0],startPixelCentre[1],  middlePixelStartCercle[0], middlePixelStartCercle[1]))
    newListSegment.append(getLine(middlePixelStartCercle[0], middlePixelStartCercle[1], pixelIntersection[0], pixelIntersection[1]))
    newListSegment.append(getLine(pixelIntersection[0], pixelIntersection[1], middlePixelEndCercle[0], middlePixelEndCercle[1]))
    newListSegment.append(getLine(middlePixelEndCercle[0], middlePixelEndCercle[1], endPixelCentre[0], endPixelCentre[1]))

    print(newListSegment)
    return newListSegment


def findPixelWithBestAngle(d, maxPixel, startPixel):
    x1 = startPixel[0]
    y1 = startPixel[1]
    x2 = maxPixel[0]
    y2 = maxPixel[1]

    cercle = testCercle(d, startPixel)

    print("findPixelWithBestAngle")
    res_tmp = getLine(x1, y1, x2, y2)
    for pixel in res_tmp:
        testInitPattern[pixel[1]][pixel[0]]=7

    for line in testInitPattern:
        print(line)
    print(res_tmp)


def calculNorme(dx, dy):
    return numpy.sqrt(dx * dx + dy * dy)


def calculProduitScalaire(dx1, dy1, dx2, dy2):
    return dx1*dx2 + dy1*dy2



def calculAngle(pixelBegin, pixelMiddle, pixelEnd):


    dx1 = (pixelBegin[0]- pixelMiddle[0])
    dy1 = (pixelBegin[1]- pixelMiddle[1])
    dx2 = (pixelEnd[0]- pixelMiddle[0])
    dy2 = (pixelEnd[1]- pixelMiddle[1])


    produitScalaire = calculProduitScalaire(dx1, dy1, dx2, dy2)
    normeP1 = calculNorme(dx1, dy1)
    normeP2 = calculNorme(dx2, dy2)

    cos_angle = round(produitScalaire / (normeP1*normeP2),3)

    radiant = math.acos(cos_angle)

    angle_degree = math.degrees(radiant)

    return round(angle_degree, 1)





def koshCreator(koshValueMax, currentKoshValue, currentKosh):

    remplissageDiffusion(testInitPattern)
    resetMatrice(currentKosh)

    if koshValueMax - currentKoshValue < 0:
        traceKosh(currentKosh)

        return currentKosh

    else:
        d = calculDistance(currentKoshValue)
        d = math.ceil(d)

        newKosh = []
        for segment in currentKosh:

            newListSegment = splitSegment(segment, d)

            for segment in newListSegment:
                newKosh.append(segment)



        traceKosh(newKosh)

     #   remplissageDiffusion(testInitPattern)

        return koshCreator(koshValueMax, currentKoshValue+1, newKosh)



def testCercle(rayon, pixelCentre):


    start_X = pixelCentre[0]
    start_Y = pixelCentre[1]
    listPixelCercle = []

    x = 0
    y = int(rayon)
    d = 5 - 4.0 * rayon

    listPixelCercle.append((x + start_X, y + start_Y))
    listPixelCercle.append((y + start_X, x + start_Y))
    listPixelCercle.append((-x + start_X, y + start_Y))
    listPixelCercle.append((-y + start_X, x + start_Y))
    listPixelCercle.append((x + start_X, -y + start_Y))
    listPixelCercle.append((y + start_X, -x + start_Y))
    listPixelCercle.append((-x + start_X, -y + start_Y))
    listPixelCercle.append((-y + start_X, -x + start_Y))

    while (y > x):

        if d > 0:
            y = y - 1
            d = d - 8.0 * y

        x = x + 1
        d = d + 8.0 * x + 4.0

        listPixelCercle.append((x + start_X, y + start_Y))
        listPixelCercle.append((y + start_X, x + start_Y))
        listPixelCercle.append((-x + start_X, y + start_Y))
        listPixelCercle.append((-y + start_X, x + start_Y))
        listPixelCercle.append((x + start_X, -y + start_Y))
        listPixelCercle.append((y + start_X, -x + start_Y))
        listPixelCercle.append((-x + start_X, -y + start_Y))
        listPixelCercle.append((-y + start_X, -x + start_Y))

    return listPixelCercle


def remplissageDiffusion(pattern):

    listPixelContent = []
    decalePixel(size_matrice-2, size_matrice-2, pattern, listPixelContent)


def decalePixel(x, y, pattern, listPixelForme):
    if x <= size_matrice - 1 and y <= size_matrice - 1 and x >= 0 and y >= 0:

        if (x, y) not in listPixelForme:

            if pattern[y][x] != 1:
                pattern[y][x] = 2
                listPixelForme.append((x, y))
               # print("FLAG")

                decalePixel(x + 1, y, pattern, listPixelForme)
                decalePixel(x, y + 1, pattern, listPixelForme)
                decalePixel(x - 1, y, pattern, listPixelForme)
                decalePixel(x, y - 1, pattern, listPixelForme)



def getLine(x1, y1, x2, y2):



    res = []
    dx = x2 - x1
    if dx != 0:
        if dx > 0:
            dy = y2 - y1
            if dy != 0:

                if dy > 0:

                    if dx >= dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1,y1) not in res:
                            res.append((x1, y1))
                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 + 1
                            e = e - dx

                            if e < 0:
                                x1 = x1 + 1
                                e = e + dy

                else:

                    if dx >= -dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    if (x1, y1) not in res:
                        res.append((x1, y1))

                    x1 = x1 + 1


        else:

            dy = y2 - y1
            if dy != 0:

                if dy > 0:
                    if -dx >= dy:
                        # 4eme octant

                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:

                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 + 1
                            e = e + dx

                            if e <= 0:
                                x1 = x1 - 1
                                e = e + dy
                else:
                    # 5eme octant
                    if dx <= dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                if (x1, y1) not in res:
                    res.append((x1, y1))

                while x1 != x2:
                    x1 = x1 - 1
                    if (x1, y1) not in res:
                        res.append((x1, y1))

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    if (x1, y1) not in res:
                        res.append((x1, y1))

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    if (x1, y1) not in res:
                        res.append((x1, y1))


    res.append((x1, y1))
    return res







if __name__ == '__main__':
    testAlgo()
=======
import numpy
import math




testInitPattern = [

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

size_matrice = 33
pixelStart = (0, 28)

res_tmp = []


def testAlgo():
    solution_user = doExercice(testInitPattern, 2)



def trouverPixelAvecLePlusDePixelAdjacent(pixelCercle, centreCercle, segment, d):

    listPixelAdjMax = ((None,None),[])

    for pixel in pixelCercle:


        listPixelAdj = (pixel, trouverPixelAdjacent(pixel, segment))


        if len(listPixelAdj[1]) > len(listPixelAdjMax[1]):
            listPixelAdjMax = listPixelAdj


    #on prend le 1er pixel
    bestPixelListe = listPixelAdjMax[1]
    maxPixel = None
    maxDistance = 0

    if len(bestPixelListe) == 0:
        for pixel in pixelCercle:
            testInitPattern[pixel[1]][pixel[0]] = 6

    for pixel in bestPixelListe:
        currentPixelValue = calculDistanceNewSegment(pixel, centreCercle)

        if abs(d-currentPixelValue[1]) < abs(d-maxDistance):
            maxDistance = currentPixelValue[1]
            maxPixel = currentPixelValue[0]


    return maxPixel



def trouverPixelAvecLePlusDePixelAdjacentCercle(pixelsCercle, centreCercle, listePixelCercle, d):

    listPixelAdjMax = ((None,None),[])


    for pixel in pixelsCercle:
        listPixelAdj = (pixel, trouverPixelAdjacentCercle(pixel, listePixelCercle))

        if len(listPixelAdj[1]) > len(listPixelAdjMax[1]) and testInitPattern[pixel[1]][pixel[0]] !=2:
            listPixelAdjMax = listPixelAdj

    #on prend le 1er pixel
    bestPixelListe = listPixelAdjMax[1]
    maxPixel = None
    maxDistance = 0


    if len(bestPixelListe) == 0:
        for pixel in pixelsCercle:
            testInitPattern[pixel[1]][pixel[0]] = 6

    for pixel in bestPixelListe:
        currentPixelValue = calculDistanceNewSegment(pixel, centreCercle)

        if abs(d-currentPixelValue[1]) < abs(d-maxDistance):
            maxDistance = currentPixelValue[1]
            maxPixel = currentPixelValue[0]


    return maxPixel





def trouverPixelAdjacentCercle(pixel, listePixelCercle):
    x = pixel[0]
    y = pixel[1]


    listPixel = []

    if x <= size_matrice - 1 and y <= size_matrice - 1 and x >= 0 and y >= 0:

                if (x + 1, y) in listePixelCercle:
                    listPixel.append((x + 1, y))

                if (x-1,y) in listePixelCercle:
                    listPixel.append((x - 1, y))

                if (x, y - 1) in listePixelCercle:
                    listPixel.append((x, y - 1))

                if (x, y + 1) in listePixelCercle:
                    listPixel.append((x, y + 1))



    return listPixel




def calculDistanceNewSegment(pixel, finalPixel):

    x0 = pixel[0]
    y0 = pixel[1]

    x1 = finalPixel[0]
    y1 = finalPixel[1]


    xd = abs(x1 - x0)
    yd = abs(y1 - y0)

    d = math.sqrt(xd*xd+yd*yd)
    return (pixel,d)


def trouverPixelAdjacent(pixel, segment):
    x = pixel[0]
    y = pixel[1]
   # print("x" + str(x))
  #  print("y" + str(y))

    listPixel = []

    if x <= size_matrice - 1 and y <= size_matrice - 1 and x >= 0 and y >= 0:

                if (x + 1, y) in segment:
                    listPixel.append((x + 1, y))

                if (x + 1, y + 1) in segment:
                    listPixel.append((x + 1, y + 1))

                if (x + 1, y - 1) in segment:
                    listPixel.append((x + 1, y - 1))

                if (x-1,y) in segment:
                    listPixel.append((x - 1, y))

                if (x - 1, y - 1) in segment:
                    listPixel.append((x - 1, y - 1))

                if (x - 1, y + 1) in segment:
                    listPixel.append((x - 1, y + 1))

                if (x, y - 1) in segment:
                    listPixel.append((x, y - 1))

                if (x, y + 1) in segment:
                    listPixel.append((x, y + 1))

#    print("listPixel")
#    print(listPixel)

    return listPixel




def resetMatrice(currentKosh):

    for linge in currentKosh:

        for pixel in linge:

            testInitPattern[pixel[1]][pixel[0]] = 0





def traceKosh(finalKosh):
    for segment in finalKosh:
        for pixel in segment:
            testInitPattern [pixel[1]][pixel[0]] = 1



def doExercice(InitPattern, koshValue):

    koshSegments = []
    kosh0 = initKosh0(pixelStart)
    koshSegments.append(kosh0)

    traceKosh(koshSegments)

    finalKosh = koshCreator(koshValue, 1, koshSegments)



    for ligne in testInitPattern:
        print(ligne)

    for pixel in res_tmp:
        testInitPattern[pixel[1]][pixel[0]]=7

    print(res_tmp)

    return finalKosh






def initKosh0(pixelStart):

    listPixelInitKosh0 = []

    id = 0
    y = pixelStart[1]

    while id < size_matrice:
        listPixelInitKosh0.append((id, y))
        id += 1

    return listPixelInitKosh0



def calculDistance(koshValue):
    return size_matrice / (3**(koshValue))



def splitSegment(segment, d):

    startPixelCentre = segment[0]
    endPixelCentre = segment[len(segment)-1]

    startCercle = testCercle(d, startPixelCentre)
    endCercle = testCercle(d, endPixelCentre)



    middlePixelStartCercle = None
    middlePixelEndCercle = None



    for pixel in startCercle:
        if pixel in segment:
            middlePixelStartCercle = pixel

    for pixel in endCercle:
        if pixel in segment:
            middlePixelEndCercle = pixel


    if middlePixelStartCercle == None:
        middlePixelStartCercle = trouverPixelAvecLePlusDePixelAdjacent(startCercle, startPixelCentre, segment, d)

    if middlePixelEndCercle == None:
        middlePixelEndCercle = trouverPixelAvecLePlusDePixelAdjacent(endCercle, endPixelCentre, segment, d)


    middleStartCercle = testCercle(d, middlePixelStartCercle)
    middleEndCercle = testCercle(d, middlePixelEndCercle)




    pixelIntersection = None

    for pixel in middleStartCercle:
        if pixel[0] < 33 and pixel[0] > 0 and pixel[1] < 33 and pixel[1] > 0 :
            if pixel in middleEndCercle and testInitPattern[pixel[1]][pixel[0]] !=2:
                pixelIntersection = pixel

    print("BISOIR")

    if pixelIntersection == None:
        print("BIJOUR")
        pixelIntersection = trouverPixelAvecLePlusDePixelAdjacentCercle(middleStartCercle ,startPixelCentre , middleEndCercle, d)


 #   for pixel in middleStartCercle:

   #     if pixel[0] < 33 and pixel[0] > 0 and pixel[1] < 33 and pixel[1] > 0:
        #    testInitPattern[pixel[1]][pixel[0]] = 3

  #  for pixel in middleEndCercle:
     #   if pixel[0] < 33 and pixel[0] > 0 and pixel[1] < 33 and pixel[1] > 0:
       #     testInitPattern[pixel[1]][pixel[0]] = 4


  #  for ligne in testInitPattern:
      #  print(ligne)


    #closeAngle = (720,(-1, -1))
    #print("closeAngle")


   # for pixelEnd in middleStartCercle:

   #     currentAngle = calculAngle(middlePixelEndCercle, middlePixelStartCercle, pixelEnd)



    #    if abs(60 - currentAngle) < abs(60 - closeAngle[0]) and \
       #         pixelEnd[0] < 33 and\
     #           pixelEnd [0] > 0 and \
      #          pixelEnd[1] < 33 and\
       #         pixelEnd [1] > 0 and \
       #         testInitPattern[pixelEnd[1]][pixelEnd[0]] != 2:


        #    closeAngle = (currentAngle,pixelEnd)
          #  print(closeAngle)


  #  closePixel = findPixelWithBestAngle(d*d, closeAngle[1], middlePixelStartCercle)

   # print(closeAngle)



    newListSegment = []

    newListSegment.append(getLine(startPixelCentre[0],startPixelCentre[1],  middlePixelStartCercle[0], middlePixelStartCercle[1]))
    newListSegment.append(getLine(middlePixelStartCercle[0], middlePixelStartCercle[1], pixelIntersection[0], pixelIntersection[1]))
    newListSegment.append(getLine(pixelIntersection[0], pixelIntersection[1], middlePixelEndCercle[0], middlePixelEndCercle[1]))
    newListSegment.append(getLine(middlePixelEndCercle[0], middlePixelEndCercle[1], endPixelCentre[0], endPixelCentre[1]))

    print(newListSegment)
    return newListSegment


def findPixelWithBestAngle(d, maxPixel, startPixel):
    x1 = startPixel[0]
    y1 = startPixel[1]
    x2 = maxPixel[0]
    y2 = maxPixel[1]

    cercle = testCercle(d, startPixel)

    print("findPixelWithBestAngle")
    res_tmp = getLine(x1, y1, x2, y2)
    for pixel in res_tmp:
        testInitPattern[pixel[1]][pixel[0]]=7

    for line in testInitPattern:
        print(line)
    print(res_tmp)


def calculNorme(dx, dy):
    return numpy.sqrt(dx * dx + dy * dy)


def calculProduitScalaire(dx1, dy1, dx2, dy2):
    return dx1*dx2 + dy1*dy2



def calculAngle(pixelBegin, pixelMiddle, pixelEnd):


    dx1 = (pixelBegin[0]- pixelMiddle[0])
    dy1 = (pixelBegin[1]- pixelMiddle[1])
    dx2 = (pixelEnd[0]- pixelMiddle[0])
    dy2 = (pixelEnd[1]- pixelMiddle[1])


    produitScalaire = calculProduitScalaire(dx1, dy1, dx2, dy2)
    normeP1 = calculNorme(dx1, dy1)
    normeP2 = calculNorme(dx2, dy2)

    cos_angle = round(produitScalaire / (normeP1*normeP2),3)

    radiant = math.acos(cos_angle)

    angle_degree = math.degrees(radiant)

    return round(angle_degree, 1)





def koshCreator(koshValueMax, currentKoshValue, currentKosh):

    remplissageDiffusion(testInitPattern)
    resetMatrice(currentKosh)

    if koshValueMax - currentKoshValue < 0:
        traceKosh(currentKosh)

        return currentKosh

    else:
        d = calculDistance(currentKoshValue)
        d = math.ceil(d)

        newKosh = []
        for segment in currentKosh:

            newListSegment = splitSegment(segment, d)

            for segment in newListSegment:
                newKosh.append(segment)



        traceKosh(newKosh)

     #   remplissageDiffusion(testInitPattern)

        return koshCreator(koshValueMax, currentKoshValue+1, newKosh)



def testCercle(rayon, pixelCentre):


    start_X = pixelCentre[0]
    start_Y = pixelCentre[1]
    listPixelCercle = []

    x = 0
    y = int(rayon)
    d = 5 - 4.0 * rayon

    listPixelCercle.append((x + start_X, y + start_Y))
    listPixelCercle.append((y + start_X, x + start_Y))
    listPixelCercle.append((-x + start_X, y + start_Y))
    listPixelCercle.append((-y + start_X, x + start_Y))
    listPixelCercle.append((x + start_X, -y + start_Y))
    listPixelCercle.append((y + start_X, -x + start_Y))
    listPixelCercle.append((-x + start_X, -y + start_Y))
    listPixelCercle.append((-y + start_X, -x + start_Y))

    while (y > x):

        if d > 0:
            y = y - 1
            d = d - 8.0 * y

        x = x + 1
        d = d + 8.0 * x + 4.0

        listPixelCercle.append((x + start_X, y + start_Y))
        listPixelCercle.append((y + start_X, x + start_Y))
        listPixelCercle.append((-x + start_X, y + start_Y))
        listPixelCercle.append((-y + start_X, x + start_Y))
        listPixelCercle.append((x + start_X, -y + start_Y))
        listPixelCercle.append((y + start_X, -x + start_Y))
        listPixelCercle.append((-x + start_X, -y + start_Y))
        listPixelCercle.append((-y + start_X, -x + start_Y))

    return listPixelCercle


def remplissageDiffusion(pattern):

    listPixelContent = []
    decalePixel(size_matrice-2, size_matrice-2, pattern, listPixelContent)


def decalePixel(x, y, pattern, listPixelForme):
    if x <= size_matrice - 1 and y <= size_matrice - 1 and x >= 0 and y >= 0:

        if (x, y) not in listPixelForme:

            if pattern[y][x] != 1:
                pattern[y][x] = 2
                listPixelForme.append((x, y))
               # print("FLAG")

                decalePixel(x + 1, y, pattern, listPixelForme)
                decalePixel(x, y + 1, pattern, listPixelForme)
                decalePixel(x - 1, y, pattern, listPixelForme)
                decalePixel(x, y - 1, pattern, listPixelForme)



def getLine(x1, y1, x2, y2):



    res = []
    dx = x2 - x1
    if dx != 0:
        if dx > 0:
            dy = y2 - y1
            if dy != 0:

                if dy > 0:

                    if dx >= dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1,y1) not in res:
                            res.append((x1, y1))
                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 + 1
                            e = e - dx

                            if e < 0:
                                x1 = x1 + 1
                                e = e + dy

                else:

                    if dx >= -dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    if (x1, y1) not in res:
                        res.append((x1, y1))

                    x1 = x1 + 1


        else:

            dy = y2 - y1
            if dy != 0:

                if dy > 0:
                    if -dx >= dy:
                        # 4eme octant

                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:

                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 + 1
                            e = e + dx

                            if e <= 0:
                                x1 = x1 - 1
                                e = e + dy
                else:
                    # 5eme octant
                    if dx <= dy:
                        e = dx
                        dx = 2 * e
                        dy = dy * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while x1 != x2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if (x1, y1) not in res:
                            res.append((x1, y1))

                        while y1 != y2:
                            if (x1, y1) not in res:
                                res.append((x1, y1))

                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                if (x1, y1) not in res:
                    res.append((x1, y1))

                while x1 != x2:
                    x1 = x1 - 1
                    if (x1, y1) not in res:
                        res.append((x1, y1))

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    if (x1, y1) not in res:
                        res.append((x1, y1))

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    if (x1, y1) not in res:
                        res.append((x1, y1))


    res.append((x1, y1))
    return res







if __name__ == '__main__':
    testAlgo()
>>>>>>> 354f19a575684013794fb04328dd9be333f0c155:comparaisonKosh.py
