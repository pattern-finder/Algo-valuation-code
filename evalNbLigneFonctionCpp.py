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
        functionContent = functionContent.replace(',', ', ')
        x = functionContent.split(", ")

        for content in x:
            listContentSplit2.append(content)
            if not set('~!@#$%^&*()+.{}":;\'+$').intersection(content):

                if "[" in content:
                    newContent = ""
                    id=0
                    finishExtractVarFromTable = False

                    while id < len(content) and not finishExtractVarFromTable:
                        if content[id] == "[":
                            finishExtractVarFromTable = True

                        else:
                            newContent += content[id]
                        id +=1

                    content = newContent

                if re.search(PATERN_VARIABLE[0], content) != None or re.search(PATERN_VARIABLE[1], content) != None or re.search(PATERN_VARIABLE[2], content) != None:

                        listContentSplit.append(content)


    for varaiblePart in listContentSplit:

        if ">" in varaiblePart:
            parts = varaiblePart.split(">")
            parts[len(parts)-2] +=">"
        else:
            parts = varaiblePart.split(" ")

        i = 0
        type=""

        while i < len(parts) -1:
            type = type+parts[i]
            i +=1

        type = re.sub(' ', '', type)
        variable = re.sub(' ', '', parts[len(parts)-1])
        listVariable.append((type, variable))


    return listVariable



def findVariableDeclare(ligne):
    """
    :param ligne: représente une ligne de code
    :return: retour le la liste des variable au seins d'une fonction
    """

    listVariable = []
    type = ""
    list = []

    if True:
        i = 0
        find = False

        while i < len(ligne) and not find:

            if ligne[i] == "=":

                notFind = True
                findSeparator = True
                permissionParcourtWord = False

                k = i
                var = ""
                typeVar = ""
                listVariableTransition = []
                inTab = False

                while k > 0 and notFind:

                    if ligne[k] == " ":

                        permissionParcourtWord = False

                        if var != "":
                            listVariableTransition.append(var)

                            var = ""

                    if ligne[k] == ",":

                        findSeparator = True
                        permissionParcourtWord = False

                        if var != "":
                            listVariableTransition.append(var)
                            var = ""

                    if ligne[k] == "]":
                        inTab= True

                    if ligne[k] == "/":
                        if len(ligne) > k+1:
                            if ligne[k+1] == "/" or ligne[k+1] == "*":

                                notFind = False

                    #Si on trouve un signe arpès avoir trouvé un séparateur ou qu'on est en train de parcourir un mot
                    if ligne[k] != "," and ligne[k] != " " and k != i and not inTab:

                        if findSeparator or permissionParcourtWord:
                            findSeparator = False
                            permissionParcourtWord = True
                            var = ligne[k]+var

                        else:
                            notFind = False


                    if ligne[k] == "[":
                        inTab = False


                    if not notFind:
                        type = ""
                        while k > 0 and ligne[k] != " ":
                            type = ligne[k]+type
                            k -=1


                        for variable in listVariableTransition:
                            if not set('[~!@#$%^&*()+.{}":;\']+$').intersection(type) and not set('[~!@#$%^&*()+.{}":;\']+$').intersection(variable) :
                                type = re.sub(' ', '', type)
                                variable = re.sub(' ', '', variable)
                                typeVar = (type, variable)

                                if typeVar not in listVariable:
                                    listVariable.append(typeVar)

                    k -= 1

            elif ligne[i] == ";" and "=" not in ligne:
                line=""
                line = re.findall(r'\s{0,}[A-Za-z0-9_]{1,}\s{1,}[A-Za-z0-9_]{1,};', ligne)

                if line != [] and "return" not in line[0]:

                    line = re.sub(';', '', line[0])
                    ligneTab = line.split(" ")

                    u = 0
                    type = ""
                    var = ""
                    while u<len(ligneTab) and line != "":
                        if ligneTab[u] != '':
                            if type == '':
                                type = ligneTab[u]
                            else:
                                var = ligneTab[u]
                        u +=1
                    type = re.sub(' ', '', type)
                    var = re.sub(' ', '', var)

                    typeVar = (type,var)

                    if typeVar not in listVariable:
                        listVariable.append(typeVar)

            i += 1

    return listVariable





def update_block(newBlock, blockCodes):
    if newBlock in blockCodes:
        blockCodes[newBlock] += 1

    else:
        blockCodes.update({newBlock: 1})

    return blockCodes


def find_block(line):
    """
    :param: line: représente le code à analyser
    :return retourne les différents blocks représentant ce code (fonction while for if ..)
    """

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




def find_function(line):
    """
    :param: line: représente le code à analyser
    :return retourne les différents blocks représentant ce code (fonction while for if ..)
    """

    blockCodes = []
    i = 0
    cptAcollade = 0
    newBlock=""
    addAblock = False

    while i < len(line):

        if line[i] == "{":

            cptAcollade += 1
            newBlock += line[i]
            addAblock = True
            i +=1

        while cptAcollade != 0 and newBlock != "" and i < len(line):

            if line[i] == "{":
                cptAcollade += 1

            elif line[i] == "}":
                cptAcollade -= 1

            if addAblock:
                newBlock += line[i]

            if cptAcollade == 0:

                blockCodes.append(newBlock)
                newBlock = ""
            i +=1

        i +=1

    return blockCodes



def rename_variable(line, listVariableRename):

    listType = []
    i = 0

    while i < len(listVariableRename):

            type = listVariableRename[i][0]
            if type not in listType:
                listType.append(type)

                listCurrentVar = []

                for variable in listVariableRename:

                    if variable[0] == type:
                        listCurrentVar.append(variable[1])


                line = line.replace(type, "")

                for variable in listCurrentVar:

                    ###gestion var++ et var--
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\+\+', type+"="+type+"+1", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\-\-', type+"="+type+"-1", line)

                    line = re.sub(r'\s{1,}'+variable+r'\s{1,}', type, line)

                    ###gestion de opérateur mathématique
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}-', type+"-", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\+', type+"+", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\*', type+"*", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\\', type+"|divide|", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}=', type+"=", line)

                    ###gestion des symbile []
                    line = re.sub(r'\[\s{0,}'+variable+r'\s{0,}\]', "["+type+"]", line)

                    ###gestion de symbole ;
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,};', type+";", line)

                    ###gestion de symbole .
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\.', type+".", line)

                    ###gestion de symbole [
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\[', type+"[", line)

                    ###gestion des symboles < >
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}<', type+"<", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}>', type+">", line)
                    line = re.sub(r'>\s{0,}'+variable+r'\s{0,}>', ">"+type+">", line)
                    line = re.sub(r'<\s{0,}'+variable+r'\s{0,}<', "<"+type+"<", line)
                    line = re.sub(r'>\s{0,}'+variable+r'\s{0,}<', ">"+type+"<", line)
                    line = re.sub(r'<\s{0,}'+variable+r'\s{0,}>', "<"+type+">", line)

                    ###gestion du séparateur ","
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,},', type+",", line)
                    line = re.sub(r',\s{0,}'+variable+r'\s{0,},', ","+type+",", line)
                    line = re.sub(r',\s{0,}'+variable+r'\s{0,}=', ","+type+"=", line)
                    line = re.sub(r',\s{0,}'+variable+r'\s{0,}\)', ","+type+")", line)

                    ###gestion des symbole ( )
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}\)', type+")", line)
                    line = re.sub(r'\(\s{0,}'+variable+r'\s{0,},', "("+type+",", line)
                    line = re.sub(r'\(\s{0,}'+variable+r'\s{0,}\)', "("+type+")", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}!', type+"!", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}<', type+"<", line)
                    line = re.sub(r'\s{0,}'+variable+r'\s{0,}>', type+">", line)

            i += 1

    return line






def sanitize_list(liste_variable):
    """
    :param liste_variable: représente la liste des variables du code
    :return: retourne la liste des variables après avoir ajouté un espace après le type de la variable. Permet de différencier les types Matrice et collection<Matrice>
    """

    id = 0
    for elt in liste_variable:
        cpt = elt[0].count('>')

        if cpt == 0:
            newElt = (elt[0] + " ", elt[1])
            elt = newElt
            liste_variable[id] = newElt

        id += 1

    return liste_variable



def remove_comentary(lignes):
    """
    :param liste_variable: représente la liste des variables du code
    :return: retourne la liste des variables après avoir ajouté un espace après le type de la variable. Permet de différencier les types Matrice et collection<Matrice>
    """
    long_comment = False
    code_without_comentary = []

    for ligne in lignes:

        if "//" in ligne:
            tab_line = ligne.split("//")
            code_without_comentary.append(tab_line[0])

        elif "/*" in ligne and "*/" in ligne:
            tab_line1 = ligne.split("/*")
            tab_line2 = ligne.split("*/")
            new_line = tab_line1[0] + tab_line2[len(tab_line2)-1]
            code_without_comentary.append(new_line)

        elif "/*" in ligne:
            tab_line = ligne.split("/*")
            code_without_comentary.append(tab_line[0])
            long_comment = True

        elif "*/" in ligne:
            tab_line = ligne.split("*/")
            code_without_comentary.append(tab_line[len(tab_line)-1])
            long_comment = False


        elif not long_comment:
            code_without_comentary.append(ligne)



    return code_without_comentary


if __name__ == '__main__':

    listFunction = []
    listVariableRename = []
    lastListVariableRename = []

    listVarBlock = []
    filin = open("userCode.cpp", "r")
    lignes = filin.readlines()

    scopeCodeUser = False
    firstInsert = False
    long_comment = False

    lignesCompacte = ""
    newBlock = []
    functionCode = ""

    lignes = remove_comentary(lignes)

    for ligne in lignes:

        if "#include" not in ligne and "using namespace" not in ligne:
                lignesCompacte +=ligne


    listFunctionCode = find_function(lignesCompacte)

    cpt_error = 0
    for function in listFunctionCode:
        function = function.replace(" ","")
        cpt_ligne = function.count('\n')-1

        if cpt_ligne > 0:
            print(function)

        table_rm = function.split('\n')
        cpt_rm = 0

        for ligne in table_rm:
            ligne = ligne.replace(" ","")
            if len(ligne) ==0:
                cpt_rm +=1

        if cpt_ligne-cpt_rm > 30:
            cpt_error+=1

    print(cpt_error)
    filin.close()