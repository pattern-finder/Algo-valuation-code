
### Ajouté par l'API avant l'envoie à judge0

from bibliothequePython import bib

import cv2 as cv

from bibliothequePython.bib import Matrice, Opencv, Exercice





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


    solution_user = doExercice(listPatternInit, matrice_result)
    print(solution_user)
    return exercice.assertRes(solution_user, resultat)




###Donnée à l'utilisateur


### FIN Ajouté par l'API avant l'envoie à judge0


#Consigne: Vous disposez d'une image résultat et d'une liste d'image.
#Implémentez la fonction doExercice afin de créer un algoritme capable de trouver l'image d'entrée dans la liste d'image de sortie
#
#
#Donnée: Image a trouver => matrice_result

#        Liste d'images a traiter => listMatrice

#Réponse: vous devez retourner l'id de limage dans la liste (0, 1, 2 ...) correspondant à l'image d'entrée


### Algo crée par l'utilisateur


def doExercice(listMatrice, matriceInputToFind, test):
    currentId = 0
    solutionId = -1
    test[3]=1
    CO = 0
    """   
    
    
    """
#fhgfh
    for matrice in listMatrice:#
        ligneInputPattern = 5

        equal = True
        matrice.toStringPixel()

        for lignePixel in matrice.getMatriceContent():
            colonneInputPattern = 0

            for pixel in lignePixel:

                if not comparePixel(colonneInputPattern, ligneInputPattern, matrice, matriceInputToFind):
                    equal = False

                    if equal:
                        solutionId = currentId


                colonneInputPattern = colonneInputPattern +1

            ligneInputPattern = ligneInputPattern +1

        if equal :
            solutionId = currentId

        currentId = currentId + 1
    ox = 100
    o
    return solutionId

def testAlgo():
    exercice = Exercice(resultat, nameExercice)

    return exercice

def comparePixel(x, y, matriceSource, matriceCible):
    return matriceSource.getPixel(x, y).compare(matriceCible.getPixel(x, y))

### FIN  Algo crée par l'utilisateur

if __name__ == '__main__':
    nameExercice = "comparaisonMatrice"
    resultat = 2
  #  print(testAlgo(nameExercice, resultat, nbMatriceResult))

