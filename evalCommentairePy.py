if __name__ == '__main__':

    filin = open("userCode.py", "r")
    lignes = filin.readlines()
    scopeCodeUser = False

    nbligne = 0
    nbligneComment = 0

    for ligne in lignes:

        if "###END" == ligne[0:6]:
            scopeCodeUser = False


        if scopeCodeUser:

            if ligne != "":
              nbligne += 1

            if '#' in ligne:
                nbligneComment +=1



        if "###START" == ligne[0:8]:
            scopeCodeUser = True


    print(nbligne)
    print(nbligneComment)

    res = ""
    if (nbligneComment/nbligne)*100 > 10:
        res = "ok"
    else:
        res = "error"

    print(res)
    filin.close()