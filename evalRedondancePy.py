import re

PATERN_VARIABLE = [
    r'[A-Za-z0-9_]{1,}\s{1,}[A-Za-z0-9_]{1,}\s*',
    r'[A-Za-z0-9_]{1,}\s{0,}<[A-Za-z0-9_]{1,}>\s{0,}[A-Za-z0-9_]{1,}',
    r'[A-Za-z0-9_]{1,}\s{1,}[A-Za-z0-9_]{1,}\s{1,}[A-Za-z0-9_]{1,}',

    r'[A-Za-z0-9_]{1,}\s{1,}[A-Za-z0-9_]{1,}\s{0,};',
    r'[A-Za-z0-9_]{1,}\s*<[A-Za-z0-9_]{1,}>\s*[A-Za-z0-9_]{0,};',
    r'[A-Za-z0-9_]{1,}\s{1,}[A-Za-z0-9_]{1,}\s{1,}[A-Za-z0-9_]{0,};',
]



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


def update_block(newBlock, blockCodes):
    if newBlock in blockCodes:
        blockCodes[newBlock] += 1

    else:
        blockCodes.update({newBlock: 1})

    return blockCodes


def find_indentation(line):

    cpt = 0
    while cpt < len(line):

        symbole = line[cpt]

        if symbole == " ":
            cpt +=1

        elif symbole == "":
            return -1

        elif symbole == "\n":
            return -1

        elif symbole == "#":
            return -1

        else:
            return cpt


    return cpt


def find_block(code):
    """
    :param: line: représente le code à analyser
    :return retourne les différents blocks représentant ce code (fonction while for if ..)
    """
    listBlock = {}
    i = 0
    lastIndentationValue=0
    currentIndentationValue = 0
    blockCodes = ""
    save=0

    for line in code:

        lastIndentationValue = save
        currentIndentationValue = find_indentation(line)

        if currentIndentationValue > lastIndentationValue :

            k=i


            blockCreate = False
            blockCodes = ""
            save = find_indentation(line)

            while not blockCreate and k < len(code):

                linebis = code[k]
                newVal = find_indentation(linebis)

                if newVal != -1:
                    currentIndentationValue = newVal


                    if currentIndentationValue > lastIndentationValue:
                        blockCodes = blockCodes+linebis


                    else:
                        blockCreate = True

                k +=1

            listBlock = update_block(blockCodes, listBlock)

        else:
            if  find_indentation(line) != -1:
                save = find_indentation(line)

        i +=1


    return listBlock




def find_function(line):
    """
    :param: line: représente le code à analyser
    :return retourne les différents blocks représentant ce code (fonction while for if ..)
    """

    blockCodes = []
    i = 0
    newBlock=""
    addAblock = False

    while i < len(line):

        if len(line)>i+4:
            if line[i] == "d":
                if line[i+1] == "e":
                    if line[i + 1] == "f":
                        if line[i + 1] == " ":

                            if newBlock != "":
                                blockCodes.append(newBlock)
                                newBlock=""

        newBlock += line[i]
        i +=1

    return blockCodes



def rename_variable(line, listVariableRename):

    i = 0
    var = "var"
    lineIndentation = find_indentation(line)

    a = 0
    espace = ""
    while a < lineIndentation:
        espace += " "
        a +=1

    while i < len(listVariableRename):

            for variable in listVariableRename:

                    ###gestion var++ et var--
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\+\+', espace+var+"="+var+"+1", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\-\-', espace+var+"="+var+"-1", line)

                    line = re.sub(r'\s{1,}'+variable+r'\s{1,}', espace+var, line)

                    ###gestion de opérateur mathématique
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}-', espace+var+"-", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\+', espace+var+"+", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\*', espace+var+"*", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\\', espace+var+"|divide|", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}=', espace+var+"=", line)

                    ###gestion des symbile []
                    line = re.sub(r'\[\s{0,}'+variable+r'\s{0,}\]', espace+"["+var+"]", line)

                    ###gestion de symbole ;
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,};', espace+var+";", line)

                    ###gestion de symbole .
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\.', espace+var+".", line)

                    ###gestion de symbole [
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\[', espace+var+"[", line)
                #    line = re.sub(r'=\s{0,}'+variable+r'\s{0,}\[int\]', type+"[", line)

                    ###gestion des symboles < >
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}<', espace+var+"<", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}>', espace+var+">", line)
                    line = re.sub(r'>\s{0,}'+variable+r'\s{0,}>', espace+">"+var+">", line)
                    line = re.sub(r'<\s{0,}'+variable+r'\s{0,}<', espace+"<"+var+"<", line)
                    line = re.sub(r'>\s{0,}'+variable+r'\s{0,}<', espace+">"+var+"<", line)
                    line = re.sub(r'<\s{0,}'+variable+r'\s{0,}>', espace+"<"+var+">", line)

                    ###gestion du séparateur ","
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,},', espace+var+",", line)
                    line = re.sub(r',\s{0,}'+variable+r'\s{0,},', espace+","+var+",", line)
                    line = re.sub(r',\s{0,}'+variable+r'\s{0,}=', espace+","+var+"=", line)
                    line = re.sub(r',\s{0,}'+variable+r'\s{0,}\)', espace+","+var+")", line)

                    ###gestion des symbole ( )
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\)', espace+var+")", line)
                    line = re.sub(r'\(\s{0,}'+variable+r'\s{0,},', espace+"("+var+",", line)
                    line = re.sub(r'\(\s{0,}'+variable+r'\s{0,}\)', espace+"("+var+")", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}!', espace+var+"!", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}<', espace+var+"<", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}>', espace+var+">", line)

            i += 1

    return line



def sanitize_dict(dict):
    """
    :param liste_variable: représente la liste des variables du code
    :return: retourne la liste des variables après avoir ajouté un espace après le type de la variable. Permet de différencier les types Matrice et collection<Matrice>
    """

    sanitize_dict = {}

    for block in dict:

        sanitizeBlock = block.replace('\n', '')
        sanitizeBlock = sanitizeBlock.replace(' ', '')
        sanitize_dict = update_block(sanitizeBlock, sanitize_dict)

    return sanitize_dict




if __name__ == '__main__':

    listFunction = []
    listVariableRename = []
    lastListVariableRename = []

    listVarBlock = []
    filin = open("userCode.py", "r")
    lignes = filin.readlines()

    scopeCodeUser = False
    firstInsert = False

    lignesCompacte = []
    newBlock = []
    functionCode = ""
    listVarToRename = []

    for ligne in lignes:

        if "###END" == ligne[0:6]:
            scopeCodeUser = False
          #  listFunction.append(listVariableRename)
          #  listVariableRename= []

        if scopeCodeUser:
            ligneBis = ligne
            ligne = ligne.replace('\n', '')

            listeVarInitFunction = findVariableInFuction(ligne)
            listeVarContentFunction = []

            if listeVarInitFunction == []:
                listeVarContentFunction = findVariableDeclare(ligne)

            listVarToRename = listeVarContentFunction + listeVarInitFunction

            i = 0
            while i < len(listVarToRename):

                if listVarToRename[i] not in listVariableRename and listVarToRename[i] != "":
                    listVariableRename.append(listVarToRename[i])
                i += 1

            lignesCompacte.append(ligneBis)

        if "###START" == ligne[0:8]:
            scopeCodeUser = True



    codeRename = ""

    for ligne in lignesCompacte:
        codeRename += rename_variable(ligne, listVariableRename)



    blockCodes = find_block(lignesCompacte)

    sanitize_dict = sanitize_dict(blockCodes)


    cptRedondance = 0

    for block in sanitize_dict:
     #   print(block)
        if sanitize_dict[block] > 1:
            cptRedondance += sanitize_dict[block]-1

    print(cptRedondance)

    filin.close()