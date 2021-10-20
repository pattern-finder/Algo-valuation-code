
from evaluation_code.python.evalNbLigneFonction import excecEvalNbLigneFonction
from evaluation_code.python.evalCommentaire import excecEvalCommentaire
from evaluation_code.python.evalRedondance import excecEvalRedondance
from evaluation_code.cpp.evalRedondance import excecEvalRedondance
#from evaluation_code.cpp.evalPlagiat import excecEvalPlagiat
from evaluation_code.cpp.getTokenizeCode import excecGetTokenizeCode
from evaluation_code.python.evalPlagiat import excecEvalPlagiat
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



    codecpp="int doExercice(vector<Matrice>listPattern, vector<Pixel> listPosStart,vector<Pixel> listPosEnd ,int size_matrice){\n"\
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
    "}\n"\
    "int u(int size_matrice){\n" \
    "int idSolution=0;\n" \
    "for(unsigned int i = 0; i < listPattern.size(); i++){\n" \
    "   idSolution++;\n" \
    "}\n" \
    "return -1;\n" \
    "}"

    user_pattern=['ddoExercicelistMatrice,matriceInputToFindcurrentId=0solutionId=-1fmatriceinlistMatriceligneInputPattern=0equal=trmatrice.toStringPixelflignePixelinmatrice.getMatriceContentcolonneInputPattern=0fpixelinlignePixelincompatrePixelcolonneInputPattern,ligneInputPattern,matrice,matriceInputToFindequal=flcolonneInputPattern=colonneInputPattern+1ligneInputPattern=ligneInputPattern+1iequalsolutionId=currentIdAAA=5currentId=currentId+1returnsolutionId', 'dcompatrePixelx,y,matriceSource,matriceCiblereturnmatriceSource.getPixelx,y.comparematriceCible.getPixelx,y',
                'ddoExercicelistMatrice,matriceInputToFindcurrentId=0solutionId=-1fmatriceinlistMatriceligneInputPattern=0equal=trmatrice.toStringPixelflignePixelinmatrice.getMatriceContentcolonneInputPattern=0fpixelinlignePixelincompatrePixelcolonneInputPattern,ligneInputPattern,matrice,matriceInputToFindequal=flcolonneInputPattern=colonneInputPattern+1ligneInputPattern=ligneInputPattern+1iequalsolutionId=currentIdAAA=5currentId=currentId+1returnsolutionIddcompatrePixelx,y,matriceSource,matriceCiblereturnmatriceSource.getPixelx,y.comparematriceCible.getPixelx,y']
    codepattern="ddoExercicelistMatrice,matriceInputToFindcurrentId=0solutionId=-1fmatriceinlistMatriceligneInputPattern=0equal=trmatrice.toStringPixelflignePixelinmatrice.getMatriceContentcolonneInputPattern=0fpixelinlignePixelincompatrePixelcolonneInputPattern,ligneInputPattern,matrice,matriceInputToFindequal=flcolonneInputPattern=colonneInputPattern+1ligneInputPattern=ligneInputPattern+1iequalsolutionId=currentIdAAA=5currentId=currentId+1returnsolutionId"

    user_patterncpp=['iidSolution=0funsgii=0iclistPattern.sizei++coutcclistPattern.sizeccendlMatricepattern=listPattern[i]PixelpixelStart=listPosStart[i]PixelpixelStop=listPosEnd[i]bores=testLinepixelStart.getX,pixelStart.getY,pixelStop.getX,pixelStop.getY,patternifresrtidSolutionidSolution++rt-1', 'iidSolution=0funsgii=0iclistPattern.sizei++Matricepattern=listPattern[i]PixelpixelStop=listPosEnd[i]ifresrtidSolutionidSolution++rt-1', 'idoExercicevect|cMatriceclistPattern,vect|cPixelclistPosStart,vect|cPixelclistPosEnd,isize_matriceiidSolution=0funsgii=0iclistPattern.sizei++coutcclistPattern.sizeccendlMatricepattern=listPattern[i]PixelpixelStart=listPosStart[i]PixelpixelStop=listPosEnd[i]bores=testLinepixelStart.getX,pixelStart.getY,pixelStop.getX,pixelStop.getY,patternifresrtidSolutionidSolution++rt-1idoExercicevect|cMatriceclistPattern,vect|cPixelclistPosStart,vect|cPixelclistPosEnd,isize_matriceiidSolution=0funsgii=0iclistPattern.sizei++Matricepattern=listPattern[i]PixelpixelStop=listPosEnd[i]ifresrtidSolutionidSolution++rt-1']
    codepatterncpp="iidSolution=0funsgii=0iclistPattern.sizei++coutcclistPattern.sizeccendlMatricepattern=listPattern[i]PixelpixelStart=listPosStart[i]PixelpixelStop=listPosEnd[i]bores=testLinepixelStart.getX,pixelStart.getY,pixelStop.getX,pixelStop.getY,patternifresrtidSolutionidSolution++rt-1"


    payload = {
   #     "eval variable name":excecEvalVariableNamePython(code),
    #    "eval redondance": excecEvalRedondance(codecpp),
  #    "eval plagiat": excecGetTokenizeCode(codecpp, False),
         "eval plagiat": excecEvalPlagiat(codepattern, user_pattern),

        #    "eval nb ligne fonction": excecEvalNbLigneFonctionPy(code),
    #    "eval commentaire": excecEvalCommentaire(code)
    #    "token code": excecEvalCommentaire(code)

    }

    print(payload)



