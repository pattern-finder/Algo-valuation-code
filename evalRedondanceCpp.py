import re
PATERN_VARIABLE = [
    r'^[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]{1,}$',
    r'^[A-Za-z0-9]{1,}\s*<[A-Za-z0-9]{1,}>\s*[A-Za-z0-9]*$',
    r'^[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]$'
]


def renameVariableInFuction(line):
        listVariable = []
        listType = []

        cpt = 0
        inFunction = False

        listContentinit = []
        listVarInFunction = ""

        for signe in line:

            if signe == "(":
                cpt += 1
                inFunction = True

            elif signe == ")":
                cpt -= 1

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
                    print(content)

        for varaiblePart in listContentSplit:

            if ">" in varaiblePart and " " not in varaiblePart:
                parts = varaiblePart.split(">")

            else:
                parts = varaiblePart.split(" ")


            listVariable.append((parts[0], parts[len(parts) - 1]))

        return listVariable


def findVariableDeclare(ligne):
    listVariable = []
    type = ""
    list = []

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

                   # if not notFind:
                    #    while k > 0 and notFind:
                         ###  type ###
                    k -= 1

            i += 1

    return listVariable





def update_block(newBlock, blockCodes):
    if newBlock in blockCodes:
        blockCodes[newBlock] += 1

    else:
        blockCodes.update({newBlock: 1})

    return blockCodes


def find_block(line):

    blockCodes = {}
    i = 0
    cptAcollade = 0
    newBlock=""
    addAblock = False

    while i < len(line):

        if line[i] == "{":
            cptAcollade += 1
            newBlock += line[i]
            addAblock = True

        k=i+1

        while cptAcollade != 0 and newBlock != "":

            if line[k] == "{":
                cptAcollade += 1

            elif line[k] == "}":
                cptAcollade -= 1

            if addAblock and line[k] != " ":
                newBlock += line[k]

            if cptAcollade == 0:
                blockCodes = update_block(newBlock, blockCodes)
                newBlock = ""
            k +=1

        i +=1

    return blockCodes




def rename_variable(line):


    return line



if __name__ == '__main__':

    listVariableRename = []
    listVariableRename = []

    filin = open("comparaisonMatrice.cpp", "r")
    lignes = filin.readlines()
    scopeCodeUser = False

    lignesCompacte = ""


    for ligne in lignes:

        if "///END" == ligne[0:6]:
            scopeCodeUser = False

        if scopeCodeUser:
            ligne = ligne.replace('\n', '')
            listVarToRename = renameVariableInFuction(ligne)

            i = 0
            while i < len(listVarToRename):
                if listVarToRename[i] not in listVariableRename and listVarToRename[i] != "":
                    listVariableRename.append(listVarToRename[i])
                i += 1

            lignesCompacte +=ligne

        if "///START" == ligne[0:8]:
            scopeCodeUser = True

    print(lignesCompacte)

    for var in listVariableRename:
        lignesCompacte = lignesCompacte.replace(var[0], "")
        lignesCompacte = lignesCompacte.replace(var[1], var[0])

    print(lignesCompacte)


    blockCodes = find_block(lignesCompacte)

    cptRedondance = 0
    for block in blockCodes:

        if blockCodes[block] > 1:
            cptRedondance += blockCodes[block]-1

    print(cptRedondance)

    ###RESULTAT
    filin.close()