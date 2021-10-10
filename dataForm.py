import cv2 as cv
import numpy
import math


from lib.bib import Matrice, Pixel, Opencv, Exercice

def testAlgo(nameExercice, resultat, nbMatriceResult):
    opencv = Opencv(nameExercice)
    opencv.setNumberImageResultat(nbMatriceResult)
    opencv.getNumberImage()
    opencv.extractImage()
    opencv.initSizeImage()

    exercice = Exercice(resultat, nameExercice)
    listPatternInit = opencv.initExercice(opencv.sizeImage)


    solutionUser = {
        "carré": 0,
        "rectangle": 0,
        "autre parallèlogramme": 0,

        "triangle rectangle": 0,
        "triangle équilatéral": 0,
        "triangle isocèle": 0,
        "triangle quelconque": 0,

        "polygone à 5 coté": 0,
        "polygone à 6 coté": 0,
        "polygone à 7 coté": 0,
    }

    solution_user = doExercice(listPatternInit, solutionUser, opencv.sizeImage)
    print(solution_user)
    return exercice.assertRes(solution_user, resultat)




### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne: Vous disposez d'une image contenant plusieurs formes.
#Implémentez la fonction doExercice afin de créer un algoritme capable de déterminer si une forme est un :
#carré
#rectangle
#autre parallèlogramme
#triangle rectangle
#triangle équilatéral
#triangle isocèle
#triangle quelconque
#polygone à 5 coté
#polygone à 6 coté
#polygone à 7 coté


#
#Donnée: l'image contenant les fromes, la taille de l'image et un dictionnaire python à remplire à renvoyer

#Réponse: vous devez retourner le dictionnaire contenant le nom des formes en clé et leur nombre en valeur




### Algo crée par l'utilisateur



def doExercice(listPattern,solutionUser, size_picture):


    id=0

    for pattern in listPattern:
        count_line = 0
        list_form = []

        listPixelSegment = []

        init_list_pixel_form = []
        listSegmentFormParcourtDroit = []

        currentLigne = 0
        currentColonne = 0
        pixelParcourtBalayageCurrent = (currentColonne,currentLigne)

        pixelParcourtBalayageEnd = (size_picture-1,size_picture-1)
        stop = False

        while pixelParcourtBalayageCurrent != pixelParcourtBalayageEnd and not stop:

            pixelStart = findStartFigure(pattern,pixelParcourtBalayageCurrent, list_form, size_picture)
            pixelParcourtBalayageCurrent = pixelStart

            if pixelStart != pixelParcourtBalayageEnd:



                pixelInit = pixelStart


                if pixelStart != None:
                    count_line = 0

                listPixelPolygon = trouverPlusLongChemin(pixelStart, pattern, init_list_pixel_form, pixelStart, pixelStart)
                listPixelPolygonReverse = []

                x = 1
                for pixel in listPixelPolygon:

                    listPixelPolygonReverse.append(listPixelPolygon[len(listPixelPolygon)-x])
                    x += 1




                for pixel_current in listPixelPolygon:

                    if testLine(pixelStart[0], pixelStart[1], pixel_current[0], pixel_current[1], pattern):
                        listPixelSegment.append(pixel_current)

                    else:

                        count_line = count_line + 1
                        pixelStart = pixel_current
                        listSegmentFormParcourtDroit.append(listPixelSegment)
                        initPixel = listPixelSegment[len(listPixelSegment)-1]
                        listPixelSegment = []
                        listPixelSegment.append(initPixel)
                        listPixelSegment.append(pixelStart)


                count_line = count_line + 1
                listPixelSegment.append(pixelInit)
                listSegmentFormParcourtDroit.append(listPixelSegment)
                list_form.append(listSegmentFormParcourtDroit)
                listPixelSegment=[]




                listeSegment=listSegmentFormParcourtDroit
                listAngleForme = []


                id = 1
                for first_segment in listSegmentFormParcourtDroit:

                    second_segment = listSegmentFormParcourtDroit[id]

                    angle = calculAngle(first_segment[0], first_segment[len(first_segment)-1], second_segment[len(second_segment)-1])
                    listAngleForme.append(angle)

                    id = id+1
                    if id > (len(listSegmentFormParcourtDroit)-1):
                        id = 0


                detect_forme(listeSegment, listAngleForme, solutionUser)
                listSegmentFormParcourtDroit = []

            else:
                stop = True

    id +=1

    return solutionUser





def detect_forme(listeSegment, listeAngle, solutionUser):

    if len(listeSegment) == 3:
        angle1 = listeAngle[0]
        angle2 = listeAngle[1]
        angle3 = listeAngle[2]

        if angle1 != angle2 and angle1 != angle3 and angle2 != angle3:
            solutionUser["triangle quelconque"] += 1

        elif angle1 == angle2 == angle3:
            solutionUser["triangle équilatéral"] += 1

        elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
            solutionUser["triangle isocèle"] += 1

        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            solutionUser["triangle rectangle"] += 1


    elif  len(listeSegment) == 4:
        angle1 = listeAngle[0]
        angle2 = listeAngle[1]
        angle3 = listeAngle[2]
        angle4 = listeAngle[3]

        segment1 = listeSegment[0]
        segment2 = listeSegment[1]
        segment3 = listeSegment[2]
        segment4 = listeSegment[3]

        if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 ==90:

            if len(segment1) == len(segment2) == len(segment3) == len(segment4):
                solutionUser["carré"] += 1
            else:
                solutionUser["rectangle"] += 1

        else:
            solutionUser["autre parallèlogramme"] += 1


    elif len(listeSegment) == 5:
        solutionUser["polygone à 5 coté"] += 1

    elif  len(listeSegment) == 6:



        solutionUser["polygone à 6 coté"] += 1

    elif len(listeSegment) == 7:
        solutionUser["polygone à 7 coté"] += 1

def calculNorme(dx, dy):
    return numpy.sqrt(dx * dx + dy * dy)

def calculProduitScalaire(dx1, dy1, dx2, dy2):
    return dx1*dx2 + dy1*dy2

def valAbs(a, b):

    res = b-a
    if res < 0:
        return -res
    else:
        return res


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




def trouverPlusLongChemin(pixelCurent, pattern, cheminCourant, pixelStart, insertPixel):

    cheminCourant = cheminCourant + [insertPixel]
    plusLongChemin = cheminCourant
    pixelsSuivant = trouverPixelSuivant(pixelCurent, pattern, cheminCourant)


    for pixel in pixelsSuivant:
        chemintmp = cheminCourant

        if pixel not in cheminCourant:

            nouveauChemin = trouverPlusLongChemin(pixel, pattern, chemintmp, pixelStart, pixel)

            if nouveauChemin != None:


                if len(nouveauChemin) > len(plusLongChemin):
                    plusLongChemin = nouveauChemin

    return plusLongChemin






def trouverPixelSuivant(pixelStart, pattern, cheminCourant):
    x = pixelStart[0]
    y = pixelStart[1]

    lisPotentielPixelNext = []

    if pixelIsNull(x+1, y, pattern) and (x + 1, y) not in cheminCourant:
        lisPotentielPixelNext.append((x + 1, y))

    if pixelIsNull(x, y+1, pattern) and (x, y + 1) not in cheminCourant:
        lisPotentielPixelNext.append((x, y + 1))

    if pixelIsNull(x-1, y, pattern) and (x - 1, y) not in cheminCourant:
        lisPotentielPixelNext.append((x - 1, y))

    if pixelIsNull(x, y-1, pattern) and (x, y - 1) not in cheminCourant:
        lisPotentielPixelNext.append((x, y - 1))

    if pixelIsNull(x+1, y+1, pattern) and (x + 1, y + 1) not in cheminCourant:
        lisPotentielPixelNext.append((x + 1, y + 1))

    if pixelIsNull(x-1, y-1, pattern) and (x - 1, y - 1) not in cheminCourant:
        lisPotentielPixelNext.append((x - 1, y - 1))

    if pixelIsNull(x-1, y+1, pattern) and (x - 1, y + 1) not in cheminCourant:
        lisPotentielPixelNext.append((x - 1, y + 1))

    if pixelIsNull(x+1, y-1, pattern) and (x + 1, y - 1) not in cheminCourant:
        lisPotentielPixelNext.append((x + 1, y - 1))


    return lisPotentielPixelNext







def findStartFigure(pattern, pixelstart, list_form, size_picture):

    ligne = pixelstart[1]
    colonne = pixelstart[0]



    pixelStart = None
    while ligne < size_picture:
        while colonne < size_picture:

            if pixelIsNull(colonne, ligne, pattern):
                pixelStart = (colonne, ligne)
                pixelFormNotExplore = True

                for form in list_form:
                    for segment in form:
                        if pixelStart in segment:
                            pixelFormNotExplore = False



                if pixelFormNotExplore:
                    return pixelStart





            colonne = colonne +1

        colonne = 0
        ligne = ligne +1


    return (size_picture-1, size_picture-1)






def testLine(x1, y1, x2, y2, patternTest):

    res = True
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

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while y1 != y2:
                            res = res and pixelIsNull(x1, y1, patternTest)
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

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while y1 != y2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    res = res and pixelIsNull(x1, y1, patternTest)
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

                        res = res and pixelIsNull(x1, y1, patternTest)

                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2



                        res = res and pixelIsNull(x1, y1, patternTest)

                        while y1 != y2:

                            res = res and pixelIsNull(x1, y1, patternTest)

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

                        res = res and pixelIsNull(x1, y1, patternTest)
                        while x1 != x2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        res = res and pixelIsNull(x1, y1, patternTest)

                        while y1 != y2:
                            res = res and pixelIsNull(x1, y1, patternTest)
                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                res = res and pixelIsNull(x1, y1, patternTest)

                while x1 != x2:
                    x1 = x1 - 1
                    res = res and pixelIsNull(x1, y1, patternTest)

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    res = res and pixelIsNull(x1, y1, patternTest)

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    res = res and pixelIsNull(x1, y1, patternTest)


    return res









def pixelIsNull(x, y, matriceSource):

    pixelNone = Pixel(x, y, (255, 255, 255))
    return not matriceSource.getPixel(x, y).compare(pixelNone)




### FIN  Algo crée par l'utilisateur

if __name__ == '__main__':
    nameExercice = "dataForm"

    resultat = {
        "carré": 2,
        "rectangle": 3,
        "autre parallèlogramme": 1,

        "triangle rectangle": 2,
        "triangle équilatéral": 0,
        "triangle isocèle": 2,
        "triangle quelconque": 1,

        "polygone à 5 coté": 1,
        "polygone à 6 coté": 0,
        "polygone à 7 coté": 2,
    }
    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))