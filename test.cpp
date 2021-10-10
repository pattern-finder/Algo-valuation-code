
#include <stdio.h>
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include "./bibliothequeCpp/Opencv.h"
#include "./bibliothequeCpp/Exercice.h"
#include "./bibliothequeCpp/Matrice.h"
#include "./bibliothequeCpp/Line.h"
#include "./bibliothequeCpp/Pixel.h"
// g++ comparaisonMatrice.cpp -o comparaisonMatrice `pkg-config --cflags --libs opencv4`
using namespace std;

///START

bool pixelIsNull(int x, int y, Matrice matriceSource, double cv[7]){

    int color[3] = {255,255,255};
    Pixel pixelNone = Pixel(x, y, color);

    return !matriceSource.getPixel(x, y).compare(pixelNone);
}





bool testLine(int x1, int y1, int x2, int y2, Matrice patternTest){

    bool res = true;

    int dx,dz = x2 - x1;

    if (dx != 0){
        if (dx > 0){
            int dy = y2 - y1;

            if (dy != 0){

                if (dy > 0){

                    if (dx >= dy){
                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (x1 != x2){

                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 + 1;
                            e = e - dy;

                            if (e < 0){
                                y1 = y1 + 1;
                                e = e + dx;
                            }
                        }

                    }else{
                        int e = dy;
                        dx = dx * 2;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (y1 != y2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 + 1;
                            e = e - dx;

                            if (e < 0){
                                x1 = x1 + 1;
                                e = e + dy;
                            }
                        }
                    }

                }else{

                    if (dx >= -dy){
                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (x1 != x2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 + 1;
                            e = e + dy;

                            if (e < 0){
                                y1 = y1 - 1;
                                e = e + dx;
                            }
                        }


                    }else{
                        int e = dy;
                        dx = 2 * dx;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);
                        while (y1 != y2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 - 1;
                            e = e + dx;


                            if (e > 0){
                                x1 = x1 + 1;
                                e = e + dy;
                            }
                        }
                    }
                }
            }else{
                while (x1 != x2){
                    res = res && pixelIsNull(x1, y1, patternTest);
                    x1 = x1 + 1;
                }
            }


        }else{

            int dy = y2 - y1;
            if (dy != 0){

                if (dy > 0){
                    if (-dx >= dy){
                        //4eme octant

                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (x1 != x2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 - 1;
                            e = e + dy;

                            if (e >= 0){
                                y1 = y1 + 1;
                                e = e + dx;
                            }
                        }

                    }else{
                        int e = dy;
                        dx = dx * 2;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (y1 != y2){

                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 + 1;
                            e = e + dx;

                            if (e <= 0){
                                x1 = x1 - 1;
                                e = e + dy;
                            }
                        }
                    }
                }else{
                    // 5eme octant
                    if (dx <= dy){
                        int e = dx;
                        dx = 2 * e;
                        dy = dy * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (x1 != x2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            x1 = x1 - 1;
                            e = e - dy;


                            if (e >= 0){
                                y1 = y1 - 1;
                                e = e + dx;
                            }
                        }

                    }else{
                        int e = dy;
                        dx = 2 * dx;
                        dy = e * 2;

                        res = res && pixelIsNull(x1, y1, patternTest);

                        while (y1 != y2){
                            res = res && pixelIsNull(x1, y1, patternTest);
                            y1 = y1 - 1;
                            e = e - dx;

                            if (e >= 0){
                                x1 = x1 - 1;
                                e = e + dy;
                            }
                        }
                    }
                }

            }else{
                res = res && pixelIsNull(x1, y1, patternTest);

                while (x1 != x2){
                    x1 = x1 - 1;
                    res = res && pixelIsNull(x1, y1, patternTest);
                }
            }
        }

    }else{
        int dy = y2 - y1;
        if (dy != 0){
            if (dy > 0){
                while (y1 != y2){
                    y1 = y1 + 1;
                    res = res and pixelIsNull(x1, y1, patternTest);
                }
            }
        }else{
                while (y1 != y2){
                    y1 = y1 - 1;
                    res = res and pixelIsNull(x1, y1, patternTest);
                }
            }
    }


    return res;
}




int doExercice(vector<Matrice>listPattern, vector<Pixel> listPosStart,vector<Pixel> listPosEnd ,int size_matrice){

    int idSolution=0;
    for(unsigned int i = 0; i < listPattern.size(); i++){

        cout << listPattern.size() << endl;

        Matrice pattern = listPattern[i];
        Pixel pixelStart = listPosStart[i];
        Pixel pixelStop = listPosEnd[i];

        bool res = testLine(pixelStart.getX(), pixelStart.getY(), pixelStop.getX(), pixelStop.getY(), pattern);

        if (res){
            return idSolution;
        }

        idSolution++;
    }
    return -1;
}

///END

string testAlgo(string nameExercice, int resultat, int nbMatriceResult){
    Opencv opencv = Opencv(nameExercice);
    opencv.setNumberImageResultat(nbMatriceResult);
    opencv.getNumberImage();
    opencv.extractImage();
    opencv.initSizeImage();

    Exercice exercice = Exercice(resultat, nameExercice);
    vector<Matrice> listPatternInit = opencv.initExercice();

    //tuple<int,int> listPosStart = [tuple<int,int> tup(13, 4), tuple<int,int> tup(13, 4), tuple<int,int> tup(13, 4), tuple<int,int> tup(16, 7)];
    //tuple<int,int> listPosEnd = [tuple<int,int> tup(9, 17),tuple<int,int> tup(9, 17),tuple<int,int> tup(9, 17),tuple<int,int> tup(9, 17)];

    int color1[3] = {0,0,0};
    int color2[3] = {0,0,0};
    int color3[3] = {0,0,0};
    int color4[3] = {0,0,0};
    int color5[3] = {0,0,0};
    int color6[3] = {0,0,0};
    int color7[3] = {0,0,0};
    int color8[3] = {0,0,0};


    Pixel pStart0 = Pixel(13,4,color1);
    Pixel pStart1 = Pixel(13,4,color2);
    Pixel pStart2 = Pixel(13,4,color3);
    Pixel pStart3 = Pixel(16,7,color4);
    vector<Pixel> listPosStart;
    listPosStart.push_back(pStart0);
    listPosStart.push_back(pStart1);
    listPosStart.push_back(pStart2);
    listPosStart.push_back(pStart3);


    Pixel pEnd0 = Pixel(9,17,color5);
    Pixel pEnd1 = Pixel(9,17,color6);
    Pixel pEnd2 = Pixel(9,17,color7);
    Pixel pEnd3 = Pixel(9,17,color8);
    vector<Pixel> listPosEnd;
    listPosEnd.push_back(pEnd0);
    listPosEnd.push_back(pEnd1);
    listPosEnd.push_back(pEnd2);
    listPosEnd.push_back(pEnd3);

    int solution_user = doExercice(listPatternInit, listPosStart, listPosEnd,opencv.sizeImage);

    return exercice.assertRes(solution_user, resultat);
}


int main(int argc, char *argv[]){
    string nameExercice = "comparaisonSegment";
    int resultat = 0;
    int nbMatriceResult = 0;

    cout << testAlgo(nameExercice, resultat, nbMatriceResult) << endl;
}