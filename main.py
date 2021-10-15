
from evaluation_code.python.evalNbLigneFonction import excecEvalNbLigneFonction
from evaluation_code.python.evalCommentaire import excecEvalCommentaire
from evaluation_code.python.evalRedondance import excecEvalRedondance
from evaluation_code.cpp.evalRedondance import excecEvalRedondance
from evaluation_code.cpp.evalPlagiat import excecEvalPlagiat
#from evaluation_code.python.evalPlagiat import excecEvalPlagiat

from evaluation_code.python.evalVariableName import excecEvalVariableName


if __name__ == '__main__':

    code="def doExercice(listMatrice, matriceInputToFind): \n"\
    "    currentId = 0\n"\
    "    solutionId = -1\n"\
    "    for matrice in listMatrice:\n"\
    "        ligneInputPattern = 0\n"\
    "        equal = True\n"\
    "        print("")\n"\
    "        matrice.toStringPixel()\n"\
    "        for lignePixel in matrice.getMatriceContent():\n"\
    "            colonneInputPattern = 0\n"\
    "            for pixel in lignePixel:\n"\
    "                if not compatrePixel(colonneInputPattern, ligneInputPattern, matrice, matriceInputToFind):\n"\
    "                    equal = False\n"\
    "                colonneInputPattern = colonneInputPattern +1\n"\
    "            ligneInputPattern = ligneInputPattern +1\n"\

    "        if equal :\n"\
    "            solutionId = currentId\n"\
    "            AAA = 5\n"\
    "        currentId = currentId + 1\n"\
    "    return solutionId\n"\
    "def compatrePixel(x, y, matriceSource, matriceCible):\n"\
    "    return matriceSource.getPixel(x, y).compare(matriceCible.getPixel(x, y))"



    codecpp = "int doExercice(vector<Matrice>listPattern, vector<Pixel> listPosStart,vector<Pixel> listPosEnd ,int size_matrice){\n"\
    "int idSolution=0;\n"\
    "for(unsigned int i = 0; i < listPattern.size(); i++){\n"\
    "    cout << listPattern.size() << endl;\n"\
    "    Matrice pattern = listPattern[i];\n"\
    "    Pixel pixelStart = listPosStart[i];\n"\
    "    Pixel pixelStop = listPosEnd[i];\n"\
    "    bool res = testLine(pixelStart.getX(), pixelStart.getY(), pixelStop.getX(), pixelStop.getY(), pattern);\n"\
    "    if (res){\n"\
    "        return idSolution;\n"\
    "    }\n"\
    "   idSolution++;\n"\
    "}\n" \
    "return -1;\n"\
"}"

    payload = {
   #     "eval variable name":excecEvalVariableNamePython(code),
    #    "eval redondance": excecEvalRedondance(codecpp),
        "eval plagiat": excecEvalPlagiat(codecpp),
        #    "eval nb ligne fonction": excecEvalNbLigneFonctionPy(code),
    #    "eval commentaire": excecEvalCommentaire(code)
    #    "token code": excecEvalCommentaire(code)

    }

    print(payload)



