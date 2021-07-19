### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import numpy

##ALGO:
from bibliothequePython.bib import Matrice, Pixel, Exercice, Opencv


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

    print("pattern")
    for patern in listPatternInit:
        print(patern)

    solution_user = [0, 0, 0]

    solution_user = doExercice(listPatternInit, opencv.sizeImage, solution_user)
    return exercice.assertRes(solution_user, resultat)




### FIN Ajouté par l'API avant l'envoie à judge0

#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de compter le nombre de segment par image
#
#Donnée: Liste d'images a traiter => listMatrice

#Réponse: vous devez retourner un tableau contenant le nombre de segment pour chaque image. L'id de la case correspondra au numero de la figure



### Algo crée par l'utilisateur



def doExercice(listPattern, size_matrice, resultat_utilisateur):

    idImage = 0
    for pattern in listPattern:


        count_line = 0

        listPixelSegment = []
        init_list_pixel_form = []

        pixelStart = findStartFigure(pattern, size_matrice)

        if pixelStart != None:
            count_line = 1

            listPixelForme = trouverPlusLongChemin(pixelStart, pattern, init_list_pixel_form, pixelStart, pixelStart)
            listPixelForme.append(pixelStart)

            for pixel_current in listPixelForme:

                if testLine(pixelStart[0],pixelStart[1], pixel_current[0], pixel_current[1], pattern):
                    listPixelSegment.append(pixel_current)

                else:
                    count_line = count_line + 1
                    pixelStart = pixel_current
                    initPixel = listPixelSegment[len(listPixelSegment)-1]
                    listPixelSegment = []
                    listPixelSegment.append(initPixel)
                    listPixelSegment.append(pixelStart)


        resultat_utilisateur[idImage] = count_line
        idImage += 1


    return resultat_utilisateur


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










def findStartFigure(pattern, size_matrice):

    ligne = 0
    colonne = 0

    while ligne < size_matrice:
        while colonne < size_matrice:

            if pixelIsNull(colonne, ligne, pattern):
                return (colonne, ligne)

            colonne = colonne +1

        colonne = 0
        ligne = ligne +1





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
    nameExercice = "compteSegment"
    resultat = [0, 3, 6]
    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))
