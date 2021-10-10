///START

#include <stdio.h>
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include "./bibliothequeCpp/Opencv.h"
#include "./bibliothequeCpp/Exercice.h"
#include "./bibliothequeCpp/Matrice.h"
#include "./bibliothequeCpp/Line.h"
#include "./bibliothequeCpp/Pixel.h"

using namespace std;


int doExercice(vector<Matrice> listPattern, Matrice result, int cv[3]){
    int currentId[3] = ;
    int x = 0;
    int y = 0;
    int CO = 0;
    int a,b= 0;
    int k = y<x<a;
    int k = y\a;

    for(unsigned int i = 0; i < listPattern.size(); i++){
        x = 0;
        y = 0;
/*



*/
        bool equaL = true;
        Matrice matrice = listPattern[i];
        while( y < result.getSize() && equaL){
            
            while( x < result.getSize() && equaL){

                if( ! (matrice.getPixel(x,y).compare(result.getPixel(x,y)))){

                    equaL = false;
                }
                x++;
           
            }
            x=0;
            y++;
           //
            }

             if(equaL){
                return currentId;
            }else{//
                currentId++;
        }

    }
    return -1;
}


int test(vector<Matrice> aaa, Matrice bh){
    float aty = 1;
    int ooo = 0;

}

int test(vector<hjgh> aaa, Matrice hhh){
    float aty = 1;
    int ooo = 0;
    int dx;
    if (dx!=0){

    }
}




std::string testAlgo(std::string nameExercice, int resultat, int nbMatriceResult){
    int tesTest =0;
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(resultat, nameExercice);
    Exercice(resultat, nameExercice);
    std::vector<Matrice> listPatternInit = opencv.initExercice();
    Matrice matrice_result = opencv.matriceResult();

    int solution_user = doExercice(listPatternInit, matrice_result);
    return exercice.assertRes(solution_user, resultat);
    
    return 0;
}





int main(int argc, char *argv[])
{
    //sdfsfsf
dqsdfqs
unionu
defaultd
defaultd
fsdfs
int d;
wcwxc
bibliothequeCppq
e
cwx
int z;
z
s
a
s
s







a
s
s
s
a
s
a
z
z
z
w
x
c
}
///END