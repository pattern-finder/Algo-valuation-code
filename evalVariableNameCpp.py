import re


PATERN_VARIABLE = [
    r'^[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]{1,}$',
    r'^[A-Za-z0-9]{1,}\s*<[A-Za-z0-9]{1,}>\s*[A-Za-z0-9]*$',
    r'^[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]$'
]


def findVariableDeclare(ligne):
    listVariable = []

    if "=" in ligne:
        i = 0
        find = False

        while i < len(ligne) and not find:
            if ligne[i] == "=":

                notFind = True
                findSeparator = True
                permissionParcourtWord = False

                k = i
                var = ""
                while k > 0 and notFind:

                    if ligne[k] == " ":
                        permissionParcourtWord = False

                        if var != "":
                            listVariable.append(var)
                            var = ""

                    if ligne[k] == ",":

                        findSeparator = True
                        permissionParcourtWord = False

                        if var != "":
                            listVariable.append(var)
                            var = ""


                    if ligne[k] != "," and ligne[k] != " " and k != i:

                        if findSeparator or permissionParcourtWord:
                            findSeparator = False
                            permissionParcourtWord = True
                            var = ligne[k]+var

                        else:
                            notFind = False

                    k -= 1

            i += 1

    return listVariable













def findVariableInFuction(line):
    listVariable = []
    cpt = 0
    inFunction = False

    listContentinit = []
    listVarInFunction = ""

    for signe in line:

        if signe == "(":
            cpt +=1
            inFunction = True

        elif signe == ")":
            cpt -=1

        if inFunction:
            if True and cpt > 0 and signe != "(":
                listVarInFunction += signe

            else:
                listContentinit.append(listVarInFunction)
                listVarInFunction = ""


    listContentSplit = []
    listContentSplit2 = []

    for functionContent in listContentinit:
        x = functionContent.split(", ")

        for content in x:

            listContentSplit2.append(content)
            if re.search(PATERN_VARIABLE[0], content) != None or re.search(PATERN_VARIABLE[1], content) != None or re.search(PATERN_VARIABLE[2], content) != None:

                listContentSplit.append(content)


    for varaiblePart in listContentSplit:

        if ">" in varaiblePart and " " not in varaiblePart:
            parts = varaiblePart.split(">")

        else:
            parts = varaiblePart.split(" ")

        listVariable.append(parts[len(parts)-1])


    return listVariable




def switch(variable):
    switcher = {
        len(variable) == 1: 1,              #teste si une varaible contient plus d'une lettre
        re.search(r'[A-Z]', variable[0]) != None and re.search(r'[A-Z]{'+str(len(variable))+',}', variable) == None : 1,  #teste si une varaible commence par une majuscule et que cette variable n'est pas une constante
    }


    return switcher.get(True, 0)



if __name__ == '__main__':

    filin = open("comparaisonMatrice.cpp", "r")
    lignes = filin.readlines()
    scopeCodeUser = False
    cpt = 0
    scopeCodeUser = False
    cpt = 0

    lignesCompacte = ""
    listVariable = []

    for ligne in lignes:


        if "///END" == ligne[0:6]:
            scopeCodeUser = False

        if scopeCodeUser:
            ligne = ligne.replace('\n', '')

            variable = ""
            variableDeclare = findVariableDeclare(ligne)

            for variable in variableDeclare:
                if variable != "" and variable not in listVariable:
                    listVariable.append(variable)

            variable = ""
            functionListVariable = findVariableInFuction(ligne)

            i = 0
            while i < len(functionListVariable):
                if functionListVariable[i] not in listVariable and functionListVariable[i] != "":
                    listVariable.append(functionListVariable[i])
                i += 1


            lignesCompacte +=ligne

        if "///START" == ligne[0:8]:
            scopeCodeUser = True

    error = 0
    for var in listVariable:
        error = error + switch(var)

    print(listVariable)

    ###RESULTAT
    print(error)
    filin.close()

