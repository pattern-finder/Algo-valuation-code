<<<<<<< HEAD:Python/comparaisonCarre.py
### Ajouté par l'API avant l'envoie à judge0


import cv2 as cv

from bibliothequePython.bib import Matrice, Pixel, Exercice, Opencv



def testAlgo(nameExercice, resultat, nbMatriceResult):
    opencv = Opencv(nameExercice)
    opencv.setNumberImageResultat(nbMatriceResult)
    opencv.getNumberImage()
    opencv.extractImage()
    opencv.initSizeImage()

    exercice = Exercice(resultat, nameExercice)
    listPatternInit = opencv.initExercice(opencv.sizeImage)

    start_X = int(opencv.sizeImage / 2) - 1
    start_Y = int(opencv.sizeImage / 2) - 1
    print("init ")
    print(start_X)
    print(start_Y)

    solution_user = doExercice(listPatternInit, start_X, start_Y)
    print(solution_user)
    return exercice.assertRes(solution_user, resultat)



### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern de carrée
#
#
#Donnée: Liste d'images a traiter => listMatrice
#        le centre de la figure
#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à un carré



### Algo crée par l'utilisateur

def doExercice(listPattern, start_X, start_Y):
    solutionId = -1
    id = 0
    equal = False

    for pattern in listPattern:

        posX = int(start_X)
        posY = int(start_Y)

        decalage = 0

        while posX > 0 and posY > 0 and not equal:



            if compatrePixel(posX, posY, pattern):

                taille_forme = tailleCarre(decalage)+1
                print("taille_forme")

                print(taille_forme)
                if parcourtPatternX(posX, posY, posX + taille_forme, pattern) and \
                        parcourtPatternX(posX, posY + taille_forme, posX + taille_forme, pattern) and \
                        parcourtPatternY(posX, posY, posY + taille_forme, pattern) and \
                        parcourtPatternY(posX + taille_forme, posY, posY + taille_forme, pattern):

                    equal = True
                    solutionId = id

            decalage = decalage + 1
            posX = posX - 1
            posY = posY - 1


        id = id + 1

    return solutionId





def tailleCarre(hauteur):
    return 2 * hauteur + 1



def compatrePixel(x, y, matriceSource):

    pixelNone = Pixel(x, y, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)


def parcourtPatternX(posX, posY, endX, pattern):

    if posX == endX:
        return compatrePixel(posX ,posY, pattern)
    else:
        if compatrePixel(posX ,posY, pattern):

            return parcourtPatternX(posX + 1, posY, endX, pattern)
        else:
            return False


def parcourtPatternY(posX, posY, endY, pattern):

    if posY == endY:

        return compatrePixel(posX ,posY, pattern)
    else:
        if compatrePixel(posX, posY, pattern):
            return parcourtPatternY(posX, posY + 1, endY, pattern)
        else:

            return False


### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':

    nameExercice = "comparaisonCarre"
    resultat = 2
    nbMatriceResult = 0

    print(testAlgo(nameExercice, resultat, nbMatriceResult))

=======
### Ajouté par l'API avant l'envoie à judge0


import cv2 as cv

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

    start_X = int(opencv.sizeImage / 2) - 1
    start_Y = int(opencv.sizeImage / 2) - 1

    solution_user = doExercice(listPatternInit, start_X, start_Y)
    print(solution_user)
    return exercice.assertRes(solution_user, resultat)



### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern de carrée
#
#
#Donnée: Liste d'images a traiter => listMatrice
#        le centre de la figure
#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à un carré



### Algo crée par l'utilisateur

def doExercice(listPattern, start_X, start_Y):
    solutionId = -1
    id = 0
    equal = False

    for pattern in listPattern:

        posX = int(start_X)
        posY = int(start_Y)
        decalage = 0

        while posX >= 0 and posY >= 0 and not equal:
            decalage = decalage + 1
            posX = posX - 1
            posY = posY - 1

            if compatrePixel(posX, posY, pattern):

                taille_forme = tailleCarre(decalage)+1

                if parcourtPatternX(posX, posY, posX + taille_forme, pattern) and \
                        parcourtPatternX(posX, posY + taille_forme, posX + taille_forme, pattern) and \
                        parcourtPatternY(posX, posY, posY + taille_forme, pattern) and \
                        parcourtPatternY(posX + taille_forme, posY, posY + taille_forme, pattern):

                    equal = True
                    solutionId = id


                else:
                    posX = posX - 1
                    posY = posY - 1
                    decalage = decalage + 1

        id = id + 1

    return solutionId





def tailleCarre(hauteur):
    return 2 * hauteur + 1



def compatrePixel(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)


def parcourtPatternX(posX, posY, endX, pattern):

    if posX == endX:
        return compatrePixel(posX ,posY, pattern)
    else:
        if compatrePixel(posX ,posY, pattern):

            return parcourtPatternX(posX + 1, posY, endX, pattern)
        else:
            return False


def parcourtPatternY(posX, posY, endY, pattern):

    if posY == endY:

        return compatrePixel(posX ,posY, pattern)
    else:
        if compatrePixel(posX, posY, pattern):
            return parcourtPatternY(posX, posY + 1, endY, pattern)
        else:

            return False


### FIN  Algo crée par l'utilisateur


if __name__ == '__main__':

    nameExercice = "comparaisonCarre"
    resultat = 3
    nbMatriceResult = 0

    print(testAlgo(nameExercice, resultat, nbMatriceResult))

>>>>>>> 354f19a575684013794fb04328dd9be333f0c155:comparaisonCarre.py
