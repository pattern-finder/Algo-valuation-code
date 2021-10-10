<<<<<<< HEAD:Python/comparaisonRotation.py
### Ajouté par l'API avant l'envoie à judge0


from math import *
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
    matrice_result = opencv.matriceResult(opencv.sizeImage)

    print("pattern")
    for patern in listPatternInit:
        print(patern)

    XY1 = (4, 7)
    XY2 = (18, 7)
    XY3 = (18, 15)
    XY4 = (4, 15)

    start_X = 11
    start_Y = 1

    solution_user = doExercice(listPatternInit , XY1, XY2, XY3, XY4, start_X, start_Y)
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


def doExercice(listMatrice, XY1, XY2, XY3, XY4,  start_X, start_Y):

    centreFigure=(11,11)
    idSolution = -1
    id = 0

    for pattern in listMatrice:
        angle = 0
        while angle < 180:

                XY1_bis = rotate(XY1,centreFigure, angle)

                XY2_bis = rotate(XY2,centreFigure, angle)

                XY3_bis = rotate(XY3,centreFigure, angle)

                XY4_bis = rotate(XY4,centreFigure, angle)

                res = verifLine(XY1_bis[0], XY1_bis[1], XY2_bis[0], XY2_bis[1], pattern) and \
                verifLine(XY2_bis[0], XY2_bis[1], XY3_bis[0], XY3_bis[1], pattern) and \
                verifLine(XY3_bis[0], XY3_bis[1], XY4_bis[0], XY4_bis[1], pattern) and \
                verifLine(XY4_bis[0], XY4_bis[1], XY1_bis[0], XY1_bis[1], pattern)

                if res:
                    idSolution = id

                angle = angle + 1

        id = id + 1


    print(idSolution)
    return idSolution

def rotate (M, O, angle) :

    angle = angle*pi / 180;
    xM = M[0] - O[0];
    yM = M[1] - O[1];
    x = xM * cos (angle) + yM * sin(angle) + O[0];
    y = - xM * sin(angle) + yM * cos(angle) + O[1];
    return (round(x),round(y));




def verifLine(x1, y1, x2, y2, pattern):


    dx = x2 - x1
    if dx != 0:
        if dx > 0:
            dy = y2 - y1
            if dy !=0:

                if dy > 0:

                    if dx >= dy:
                        e = dx
                        dx = 2*e
                        dy = dy *2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False
                        while  y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

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

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    if not compatrePixel(x1, y1, pattern):
                        return False

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


                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while  x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

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

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                if not compatrePixel(x1, y1, pattern):
                    return False

                while x1 != x2:
                    x1 = x1 - 1
                    if not compatrePixel( x1, y1, pattern):
                        return False

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    if not compatrePixel( x1, y1, pattern):
                        return False

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    if not compatrePixel( x1, y1, pattern):
                        return False

    return True









def tailleCarre(hauteur):
    return 2 * hauteur + 1


def printMatrice(matrice):

    for line in matrice:
        print(getLine(line, 0))


def getLine(line, pos):

    if pos < len(line):
        return str(line[pos]) + getLine(line, pos+1)

    else:
        return ""


def compatrePixel(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)



### FIN  Algo crée par l'utilisateur



if __name__ == '__main__':
    nameExercice = "comparaisonRotation"
    resultat = 2
    nbMatriceResult = 1
    print(testAlgo(nameExercice, resultat, nbMatriceResult))
=======
### Ajouté par l'API avant l'envoie à judge0


from math import *
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
    matrice_result = opencv.matriceResult(opencv.sizeImage)

    print("pattern")
    for patern in listPatternInit:
        print(patern)

    XY1 = (4, 7)
    XY2 = (18, 7)
    XY3 = (18, 15)
    XY4 = (4, 15)

    start_X = 11
    start_Y = 1

    solution_user = doExercice(listPatternInit , XY1, XY2, XY3, XY4, start_X, start_Y)
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


def doExercice(listMatrice, XY1, XY2, XY3, XY4,  start_X, start_Y):

    centreFigure=(11,11)
    idSolution = -1
    id = 0

    for pattern in listMatrice:
        angle = 0
        while angle < 180:

                XY1_bis = rotate(XY1,centreFigure, angle)

                XY2_bis = rotate(XY2,centreFigure, angle)

                XY3_bis = rotate(XY3,centreFigure, angle)

                XY4_bis = rotate(XY4,centreFigure, angle)

                res = verifLine(XY1_bis[0], XY1_bis[1], XY2_bis[0], XY2_bis[1], pattern) and \
                verifLine(XY2_bis[0], XY2_bis[1], XY3_bis[0], XY3_bis[1], pattern) and \
                verifLine(XY3_bis[0], XY3_bis[1], XY4_bis[0], XY4_bis[1], pattern) and \
                verifLine(XY4_bis[0], XY4_bis[1], XY1_bis[0], XY1_bis[1], pattern)

                if res:
                    idSolution = id

                angle = angle + 1

        id = id + 1


    print(idSolution)
    return idSolution

def rotate (M, O, angle) :

    angle = angle*pi / 180;
    xM = M[0] - O[0];
    yM = M[1] - O[1];
    x = xM * cos (angle) + yM * sin(angle) + O[0];
    y = - xM * sin(angle) + yM * cos(angle) + O[1];
    return (round(x),round(y));




def verifLine(x1, y1, x2, y2, pattern):


    dx = x2 - x1
    if dx != 0:
        if dx > 0:
            dy = y2 - y1
            if dy !=0:

                if dy > 0:

                    if dx >= dy:
                        e = dx
                        dx = 2*e
                        dy = dy *2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 + 1
                            e = e - dy

                            if e < 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False
                        while  y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

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

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 + 1
                            e = e + dy

                            if e < 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            y1 = y1 - 1
                            e = e + dx

                            if e > 0:
                                x1 = x1 + 1
                                e = e + dy
            else:
                while x1 != x2:
                    if not compatrePixel(x1, y1, pattern):
                        return False

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


                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while  x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 - 1
                            e = e + dy

                            if e >= 0:
                                y1 = y1 + 1
                                e = e + dx

                    else:
                        e = dy
                        dx = dx * 2
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

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

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while x1 != x2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            x1 = x1 - 1
                            e = e - dy

                            if e >= 0:
                                y1 = y1 - 1
                                e = e + dx

                    else:
                        e = dy
                        dx = 2 * dx
                        dy = e * 2

                        if not compatrePixel(x1, y1, pattern):
                            return False

                        while y1 != y2:
                            if not compatrePixel(x1, y1, pattern):
                                return False

                            y1 = y1 - 1
                            e = e - dx

                            if e >= 0:
                                x1 = x1 - 1
                                e = e + dy

            else:
                if not compatrePixel(x1, y1, pattern):
                    return False

                while x1 != x2:
                    x1 = x1 - 1
                    if not compatrePixel( x1, y1, pattern):
                        return False

    else:
        dy = y2 - y1
        if dy != 0:
            if dy > 0:
                while y1 != y2:
                    y1 = y1 + 1
                    if not compatrePixel( x1, y1, pattern):
                        return False

            else:
                while y1 != y2:
                    y1 = y1 - 1
                    if not compatrePixel( x1, y1, pattern):
                        return False

    return True









def tailleCarre(hauteur):
    return 2 * hauteur + 1


def printMatrice(matrice):

    for line in matrice:
        print(getLine(line, 0))


def getLine(line, pos):

    if pos < len(line):
        return str(line[pos]) + getLine(line, pos+1)

    else:
        return ""


def compatrePixel(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)



### FIN  Algo crée par l'utilisateur



if __name__ == '__main__':
    nameExercice = "comparaisonRotation"
    resultat = 2
    nbMatriceResult = 1
    print(testAlgo(nameExercice, resultat, nbMatriceResult))
>>>>>>> 354f19a575684013794fb04328dd9be333f0c155:comparaisonRotation.py
