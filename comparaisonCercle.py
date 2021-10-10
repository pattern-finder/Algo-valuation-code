<<<<<<< HEAD:Python/comparaisonCercle.py
### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import numpy

from bibliothequePython.bib import Matrice, Pixel, Opencv, Exercice


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

    start_X = int(opencv.sizeImage / 2)
    start_Y = int(opencv.sizeImage / 2)

    solution_user = doExercice(listPatternInit, start_X, start_Y)
    print(solution_user)
    print(resultat)

    return exercice.assertRes(solution_user, resultat)




### FIN Ajouté par l'API avant l'envoie à judge0



#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern de cercle
#l'algorithme a utiliser est l'algorithme de tracé de cercle de bresenham
#
#Donnée: Liste d'images a traiter => listMatrice
#        le centre de la figure
#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à un cercle de bresenham



### Algo crée par l'utilisateur
def doExercice(listPattern, start_X, start_Y):

    solutionId = 0

    for pattern in listPattern:
        r = 0

        pattern.toStringPixel()
        while r <= 11:

            x = 0
            y = int(r)
            d = 5 - 4.0*r

            res = pixelIsNull(x + start_X, y + start_Y, pattern) and \
            pixelIsNull(y + start_X, x + start_Y, pattern) and \
            pixelIsNull(-x + start_X, y + start_Y, pattern) and \
            pixelIsNull(-y + start_X, x + start_Y, pattern) and \
            pixelIsNull(x + start_X, -y + start_Y, pattern) and \
            pixelIsNull(y + start_X, -x + start_Y, pattern) and \
            pixelIsNull(-x + start_X, -y + start_Y, pattern) and \
            pixelIsNull(-y + start_X, -x + start_Y, pattern)




            while (y > x):

                if  d > 0:
                    y = y-1
                    d = d - 8.0*y

                x = x + 1
                d = d + 8.0 * x + 4.0
                res = res and pixelIsNull(x + start_X, y + start_Y, pattern) and \
                pixelIsNull(y + start_X, x + start_Y, pattern) and \
                pixelIsNull(-x + start_X, y + start_Y, pattern) and \
                pixelIsNull(-y + start_X, x + start_Y, pattern) and \
                pixelIsNull(x + start_X, -y + start_Y, pattern) and \
                pixelIsNull(y + start_X, -x + start_Y, pattern) and \
                pixelIsNull(-x + start_X, -y + start_Y, pattern) and \
                pixelIsNull(-y + start_X, -x + start_Y, pattern)

            r +=1

        if res == True:
            return solutionId

        solutionId += 1



def pixelIsNull(x, y, matriceSource):

    pixelNone = Pixel(x, y, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)






### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':

    nameExercice = "comparaisonCercle"
    resultat = 3
    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))
=======
### Ajouté par l'API avant l'envoie à judge0

import cv2 as cv
import numpy

from bibliothequePython.bib import Matrice, Pixel, Opencv, Exercice


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

    start_X = int(opencv.sizeImage / 2)
    start_Y = int(opencv.sizeImage / 2)

    solution_user = doExercice(listPatternInit, start_X, start_Y)
    print(solution_user)
    print(resultat)

    return exercice.assertRes(solution_user, resultat)




### FIN Ajouté par l'API avant l'envoie à judge0



#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern de cercle
#l'algorithme a utiliser est l'algorithme de tracé de cercle de bresenham
#
#Donnée: Liste d'images a traiter => listMatrice
#        le centre de la figure
#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à un cercle de bresenham



### Algo crée par l'utilisateur
def doExercice(listPattern, start_X, start_Y):

    solutionId = 0

    for pattern in listPattern:
        r = 0

        pattern.toStringPixel()
        while r <= 11:

            x = 0
            y = int(r)
            d = 5 - 4.0*r

            res = pixelIsNull(x + start_X, y + start_Y, pattern) and \
            pixelIsNull(y + start_X, x + start_Y, pattern) and \
            pixelIsNull(-x + start_X, y + start_Y, pattern) and \
            pixelIsNull(-y + start_X, x + start_Y, pattern) and \
            pixelIsNull(x + start_X, -y + start_Y, pattern) and \
            pixelIsNull(y + start_X, -x + start_Y, pattern) and \
            pixelIsNull(-x + start_X, -y + start_Y, pattern) and \
            pixelIsNull(-y + start_X, -x + start_Y, pattern)




            while (y > x):

                if  d > 0:
                    y = y-1
                    d = d - 8.0*y

                x = x + 1
                d = d + 8.0 * x + 4.0
                res = res and pixelIsNull(x + start_X, y + start_Y, pattern) and \
                pixelIsNull(y + start_X, x + start_Y, pattern) and \
                pixelIsNull(-x + start_X, y + start_Y, pattern) and \
                pixelIsNull(-y + start_X, x + start_Y, pattern) and \
                pixelIsNull(x + start_X, -y + start_Y, pattern) and \
                pixelIsNull(y + start_X, -x + start_Y, pattern) and \
                pixelIsNull(-x + start_X, -y + start_Y, pattern) and \
                pixelIsNull(-y + start_X, -x + start_Y, pattern)

            r +=1

        if res == True:
            return solutionId

        solutionId += 1



def pixelIsNull(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)






### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':

    nameExercice = "comparaisonCercle"
    resultat = 3
    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))
>>>>>>> 354f19a575684013794fb04328dd9be333f0c155:comparaisonCercle.py
