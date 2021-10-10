<<<<<<< HEAD:Python/comparaisonAngles.py
import math

import cv2 as cv
import numpy

from bibliothequePython.bib import Pixel, Matrice, Opencv, Exercice







def testAlgo(nameExercice, resultat, nbMatriceResult):
    opencv = Opencv(nameExercice)
    opencv.setNumberImageResultat(nbMatriceResult)
    opencv.getNumberImage()
    opencv.extractImage()
    opencv.initSizeImage()

    exercice = Exercice(resultat, nameExercice)
    listPatternInit = opencv.initExercice(opencv.sizeImage)


    dict_resultat = {
        0: 0.0,
        1: 0.0,
        2: 0.0
    }

    resultat_valide = {
        0: 90.0,
        1: 45.0,
        2: 135.0
    }

    listeListePixelParImage = [
        [(4, 2), (4, 14), (19, 14)],
        [(16, 2), (4, 14), (19, 14)],
        [(4, 8), (10, 14), (19, 14)],
    ]

    solution_user = doExercice(listPatternInit, listeListePixelParImage, dict_resultat, opencv.sizeImage)



    return exercice.assertRes(solution_user, resultat_valide)

### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne: Vous disposez l'iste d'image représentant plusieur angle.
#Implémentez la fonction doExercice afin de créer un algoritme capable de déterminer la valeur de chaque angle :


#
#Donnée: la liste d'image dont les angles sont à calculer, la liste des pixel limite des 2 segment de chaque image et un dictionnaire python à remplire à renvoyer

#Réponse: vous devez retourner le dictionnaire contenant la valeur des angles de chaque images


### Algo crée par l'utilisateur





def doExercice(listPattern, listeListePixelParImage, dict_resultat, size_matrice):

    id = 0
    for pattern in listPattern:

        listeListeInit = listeListePixelParImage[id]

        p0 = listeListeInit[0]
        p1 = listeListeInit[1]
        p2 = listeListeInit[2]

        if p0[0] >= 0 and p0[1] >= 0 and p1[0] >= 0 and p1[1] >= 0 and p2[0] >= 0 and p2[1] >= 0 and \
                p0[0] < size_matrice and p0[1] < size_matrice and p1[0] < size_matrice and p1[1] < size_matrice and p2[0] < size_matrice and p2[1] < size_matrice :

            angle = calculAngle(p0, p1, p2)

            dict_resultat[id] = angle

        id += 1
    print(dict_resultat)
    return dict_resultat

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

    dx1 = (pixelBegin[0] - pixelMiddle[0])
    dy1 = (pixelBegin[1] - pixelMiddle[1])
    dx2 = (pixelEnd[0] - pixelMiddle[0])
    dy2 = (pixelEnd[1] - pixelMiddle[1])

    produitScalaire = calculProduitScalaire(dx1, dy1, dx2, dy2)
    normeP1 = calculNorme(dx1, dy1)
    normeP2 = calculNorme(dx2, dy2)

    cos_angle = produitScalaire / (normeP1*normeP2)

    radiant = math.acos(cos_angle)

    angle_degree = math.degrees(radiant)

    return angle_degree



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







if __name__ == '__main__':

    nameExercice = "comparaisonAngle"

    resultat = {
        0: 90.0,
        1: 45.0,
        2: 135.0
    }

    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))


=======
import math

import cv2 as cv
import numpy

from bibliothequePython.bib import Pixel, Matrice, Opencv, Exercice







def testAlgo(nameExercice, resultat, nbMatriceResult):
    opencv = Opencv(nameExercice)
    opencv.setNumberImageResultat(nbMatriceResult)
    opencv.getNumberImage()
    opencv.extractImage()
    opencv.initSizeImage()

    exercice = Exercice(resultat, nameExercice)
    listPatternInit = opencv.initExercice(opencv.sizeImage)
    print("test")
    print(opencv.sizeImage)


    dict_resultat = {
        0: 0.0,
        1: None,
        2: 0.0,
        3: 0.0
    }

    resultat_valide = {
        0: 90.0,
        1: None,
        2: 45.0,
        3: 135.0
    }

    listeListePixelParImage = [
        [(4, 2), (4, 14), (19, 14)],
        [(-1, -1), (-1, -1), (-1, -1)],
        [(16, 2), (4, 14), (19, 14)],
        [(4, 8), (10, 14), (19, 14)],
    ]

    solution_user = doExercice(listPatternInit, listeListePixelParImage, dict_resultat, opencv.sizeImage)



    return exercice.assertRes(solution_user, resultat_valide)

### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne: Vous disposez l'iste d'image représentant plusieur angle.
#Implémentez la fonction doExercice afin de créer un algoritme capable de déterminer la valeur de chaque angle :


#
#Donnée: la liste d'image dont les angles sont à calculer, la liste des pixel limite des 2 segment de chaque image et un dictionnaire python à remplire à renvoyer

#Réponse: vous devez retourner le dictionnaire contenant la valeur des angles de chaque images


### Algo crée par l'utilisateur





def doExercice(listPattern, listeListePixelParImage, dict_resultat, size_matrice):

    id = 0
    for pattern in listPattern:

        listeListeInit = listeListePixelParImage[id]

        p0 = listeListeInit[0]
        p1 = listeListeInit[1]
        p2 = listeListeInit[2]

        if p0[0] >= 0 and p0[1] >= 0 and p1[0] >= 0 and p1[1] >= 0 and p2[0] >= 0 and p2[1] >= 0 and \
                p0[0] < size_matrice and p0[1] < size_matrice and p1[0] < size_matrice and p1[1] < size_matrice and p2[0] < size_matrice and p2[1] < size_matrice :

            angle = calculAngle(p0, p1, p2)

            dict_resultat[id] = angle
            print(dict_resultat[id])

        id += 1
    return dict_resultat

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

    dx1 = (pixelBegin[0] - pixelMiddle[0])
    dy1 = (pixelBegin[1] - pixelMiddle[1])
    dx2 = (pixelEnd[0] - pixelMiddle[0])
    dy2 = (pixelEnd[1] - pixelMiddle[1])

    produitScalaire = calculProduitScalaire(dx1, dy1, dx2, dy2)
    normeP1 = calculNorme(dx1, dy1)
    normeP2 = calculNorme(dx2, dy2)

    a = produitScalaire / (normeP1 * normeP2)
    cos_angle = produitScalaire / (normeP1*normeP2)

    radiant = math.acos(cos_angle)

    angle_degree = math.degrees(radiant)

    return angle_degree



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







if __name__ == '__main__':

    nameExercice = "comparaisonAngle"

    resultat = {
        0: 90.0,
        1: None,
        2: 45.0,
        3: 135.0
    }

    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))


>>>>>>> 354f19a575684013794fb04328dd9be333f0c155:comparaisonAngles.py
