import re



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
    variable = ""

    i = 0
    if line.count('def') > 0:
        start = False
        end = False

        while i < len(line):

            if line[i] == "(":
                start = True
                i=i+1


            if start and not end:

                if line[i] != "," and line[i] != ")":

                    if line[i] != " ":
                        variable += line[i]

                else:
                    listVariable.append(variable)
                    variable = ""

            if line[i] == ")":
                end = True

            i +=1

    return listVariable





def findVariableFromList(line):

    i = 0
    if line.count(' in ') > 0:
        variable = ""
        find = False
        findSpace = False

        while i < len(line):

            if line[i] == "i" and i+4 <= len(line):

                if i-1 > 0:

                    if line[i-1] == " ":

                        if line[i+1] == "n" and line[i+2] == " ":
                            find = True

            if not find:

                if line[i] != " ":

                    if findSpace:
                        findSpace = False
                        variable = ""

                    variable += ligne[i]

                else:
                    findSpace = True

            else:
                return variable

            i +=1

    return ""



def switch(variable):
    switcher = {
        len(variable) == 1: 1,              #teste si une varaible contient plus d'une lettre
        variable.lower() != variable and re.search(r'[A-Z]{' + str(len(variable)) + ',}',variable) == None : 1,  #teste si une varaible commence par une majuscule

    }

    return switcher.get(True, 0)




if __name__ == '__main__':

    filin = open("userCode.py", "r")
    lignes = filin.readlines()
    scopeCodeUser = False
    cpt = 0

    listVariable = []


    for ligne in lignes:

        if "###START" == ligne[0:8]:
            scopeCodeUser = True

        if "###END" == ligne[0:6]:
            scopeCodeUser = False


        if scopeCodeUser:

            variables = ""
            variables = findVariableDeclare(ligne)

            for variable in variables:

                if variables != "" and variable not in listVariable:
                    listVariable.append(variable)



            variable = ""
            functionListVariable = findVariableInFuction(ligne)

            i = 0
            while i < len(functionListVariable):
                if functionListVariable[i] not in listVariable:
                    listVariable.append(functionListVariable[i])
                i +=1

            variableFromList = findVariableFromList(ligne)

            if variableFromList != "":
                listVariable.append(variableFromList)


    error = 0
    for var in listVariable:
        error = error + switch(var)

    print(listVariable)

    ###RESULTAT
    print(error)
    filin.close()