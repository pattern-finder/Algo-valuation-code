import re


PATERN_VARIABLE = [
    r'^[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]{1,}$',
    r'^[A-Za-z0-9]*\s*<*[A-Za-z0-9]*>*\s*[A-Za-z0-9]*$',
    r'^[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]{1,}\s{1,}[A-Za-z0-9]$'

]



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

            k +=1

        i +=1

    return blockCodes




if __name__ == '__main__':


    filin = open("comparaisonMatrice.cpp", "r")
    lignes = filin.readlines()
    scopeCodeUser = False

    lignesCompacte = ""


    for ligne in lignes:

        if "///END" == ligne[0:6]:
            scopeCodeUser = False

        if scopeCodeUser:
            ligne = ligne.replace('\n', '')
            lignesCompacte +=ligne

        if "///START" == ligne[0:8]:
            scopeCodeUser = True


    print(lignesCompacte)
    blockCodes = find_block(lignesCompacte)

    for block in blockCodes:
        print(block)

    ###RESULTAT
    filin.close()


