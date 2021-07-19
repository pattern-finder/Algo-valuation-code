if __name__ == '__main__':

    filin = open("userCode.cpp", "r")
    lignes = filin.readlines()
    scopeCodeUser = False

    nbLigne = 0
    nbComment = 0
    longComment = False

    for ligne in lignes:

        if "///END" == ligne[0:6]:
            scopeCodeUser = False


        if scopeCodeUser:
            if ligne != "":
                nbLigne += 1

            if '//' in ligne and not longComment:
                nbComment +=1

            if '/*' in ligne:
                longComment = True

            if '*/' in ligne:
                longComment = False

            if longComment:
                nbComment += 1

        if "///START" == ligne[0:8]:
            scopeCodeUser = True


    print(nbLigne)
    print(nbComment)


    res = ""
    if nbLigne >0:

        if (nbComment/nbLigne)*100 >= 10:
            res = "ok"
        else:
            res = "error"
    else:
        res = "ok"

    print(res)
    filin.close()