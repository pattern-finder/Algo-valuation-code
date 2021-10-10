<<<<<<< HEAD:Python/comparaisonRemplissage.py
### Ajouté par l'API avant l'envoie à judge0
#JEPSEN

import cv2 as cv

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



    solution_user = doExercice(listPatternInit, opencv.sizeImage)
    return exercice.assertRes(solution_user, resultat)




### FIN Ajouté par l'API avant l'envoie à judge0

#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern remplie (dont tous les pixels intèriueurs sont noir)
#
#
#Donnée: Liste d'images a traiter => listMatrice

#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à une forme pleine


### Algo crée par l'utilisateur




def doExercice(listPatternInit,size_matrice):


    res1 = remplissageBalayage(listPatternInit, size_matrice)

    return res1





def remplissageBalayage(listPattern, size_matrice):
    idSolution = 0

    for pattern in listPattern:

        ligne = 0
        colonne = 0
        echec = False

        while ligne < size_matrice-1 and not echec:

            cpt_bordure = 0
            inForm = False

            while colonne < size_matrice-1 and not echec:

                if cpt_bordure > 2 and cpt_bordure != 0:
                    echec = True


                if pixelIsNotNull(colonne, ligne, pattern):


                    if not inForm:

                        inForm = True
                        cpt_bordure += 1

                else:

                    if inForm:

                        inForm = False
                        cpt_bordure += 1



                colonne = colonne + 1

            colonne = 0
            ligne = ligne + 1




        if not echec:
            return idSolution


        idSolution +=1


    return 0


def decalePixel(x, y, pattern, listPixelForme, size_matrice):

        if x <= size_matrice-1 and y<= size_matrice-1:

            if (x, y) not in listPixelForme :

                if pixelIsNotNull(x,y,pattern):


                    listPixelForme.append((x, y))

                    return decalePixel(x+1,y,pattern, listPixelForme, size_matrice) and \
                    decalePixel(x,y+1,pattern, listPixelForme, size_matrice) and \
                    decalePixel(x-1,y,pattern, listPixelForme, size_matrice) and \
                    decalePixel(x,y-1,pattern, listPixelForme, size_matrice)

                else:
                    return False

            else:
                return True

        else :
            return False


def pixelIsNotNull(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)




### FIN  Algo crée par l'utilisateur





if __name__ == '__main__':
    nameExercice = "comparaisonRemplissage"
    resultat = 2
    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))
=======
### Ajouté par l'API avant l'envoie à judge0
#JEPSEN

import cv2 as cv

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



    solution_user = doExercice(listPatternInit, opencv.sizeImage)
    return exercice.assertRes(solution_user, resultat)




### FIN Ajouté par l'API avant l'envoie à judge0

#Consigne: Vous disposez d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver le pattern remplie (dont tous les pixels intèriueurs sont noir)
#
#
#Donnée: Liste d'images a traiter => listMatrice

#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à une forme pleine


### Algo crée par l'utilisateur




def doExercice(listPatternInit,size_matrice):


    res1 = remplissageBalayage(listPatternInit, size_matrice)

    return res1





def remplissageBalayage(listPattern, size_matrice):
    idSolution = 0

    for pattern in listPattern:

        ligne = 0
        colonne = 0
        echec = False

        while ligne < size_matrice-1 and not echec:

            cpt_bordure = 0
            inForm = False

            while colonne < size_matrice-1 and not echec:

                if cpt_bordure > 2 and cpt_bordure != 0:
                    echec = True


                if pixelIsNotNull(colonne, ligne, pattern):


                    if not inForm:

                        inForm = True
                        cpt_bordure += 1

                else:

                    if inForm:

                        inForm = False
                        cpt_bordure += 1



                colonne = colonne + 1

            colonne = 0
            ligne = ligne + 1




        if not echec:
            return idSolution


        idSolution +=1


    return 0


def decalePixel(x, y, pattern, listPixelForme, size_matrice):

        if x <= size_matrice-1 and y<= size_matrice-1:

            if (x, y) not in listPixelForme :

                if pixelIsNotNull(x,y,pattern):


                    listPixelForme.append((x, y))

                    return decalePixel(x+1,y,pattern, listPixelForme, size_matrice) and \
                    decalePixel(x,y+1,pattern, listPixelForme, size_matrice) and \
                    decalePixel(x-1,y,pattern, listPixelForme, size_matrice) and \
                    decalePixel(x,y-1,pattern, listPixelForme, size_matrice)

                else:
                    return False

            else:
                return True

        else :
            return False


def pixelIsNotNull(x, y, matriceSource):

    pixelNone = Pixel(x, x, (255, 255, 255))

    return not matriceSource.getPixel(x, y).compare(pixelNone)




### FIN  Algo crée par l'utilisateur





if __name__ == '__main__':
    nameExercice = "comparaisonRemplissage"
    resultat = 2
    nbMatriceResult = 0
    print(testAlgo(nameExercice, resultat, nbMatriceResult))
>>>>>>> 354f19a575684013794fb04328dd9be333f0c155:comparaisonRemplissage.py
