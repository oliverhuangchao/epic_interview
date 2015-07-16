#include "basic.h"
 /*16.     Snake Sequence 
 You are given a grid of numbers. A snakesequence is made up of adjacent numbers such 
 that for each number, the numberon the right or the number below it is +1 or -1 its value. 
 For example,  
 1 3 2 6 8  
 -9 7 1 -1 2  
 1 5 0 1 9  
 In this grid, (3, 2, 1, 0, 1) is a snake sequence. Given a grid, find thelongest snake 
 sequences and their lengths (so there can be multiple snakesequences with the maximum 
 length). */

void dfs(vector<vector<int>> &matrix,int i,int j,vector<vector<int>> &result,vector<int> &path,int value){
    //int value = matrix[i][j];
    // go to rigth
    if(j != matrix[0].size()-1 and abs(matrix[i][j+1] - value)==1){
        int tmp =  matrix[i][j+1];
        matrix[i][j+1] = -100;
        path.push_back(tmp);
        dfs(matrix,i,j+1,result,path,tmp);
        path.pop_back();
    }

    // go to the down
    if(i != matrix.size()-1 and abs(matrix[i+1][j] - value)==1){
        int tmp =  matrix[i+1][j];
        matrix[i+1][j] = -100;
        path.push_back(tmp);
        dfs(matrix,i+1,j,result,path,tmp);
        path.pop_back();
    }

    // go to the left
    if(j != 0 and abs(matrix[i][j-1] - value)==1){
        int tmp =  matrix[i][j-1];
        matrix[i][j-1] = -100;
        path.push_back(tmp);
        dfs(matrix,i,j-1,result,path,tmp);
        path.pop_back();
    }

    // go the the up
    if(i != 0 and abs(matrix[i-1][j] - value)==1){
        int tmp =  matrix[i-1][j];
        matrix[i-1][j] = -100;
        path.push_back(tmp);
        dfs(matrix,i-1,j,result,path,tmp);
        path.pop_back();
    }
    result.push_back(path);
    //path.clear();
    return;
    //return 1;     
}

void findmax(){
    int x[] = {1, 3, 2, 6, 8, -9, 7, 1, -1, 2, 1, 5, 0, 1, 9};
    vector<vector<int>> matrix = getMatrix(x,3,5);
    //print(matrix.size());
    //print(matrix[0].size());
    vector<vector<int>> result;
    vector<int> path;
    print(matrix);
    for(int i=0;i<matrix.size();i++){
        for(int j=0;j<matrix[0].size();j++){
            if(matrix[i][j] != -100){
                path.push_back(matrix[i][j]);
                int value = matrix[i][j];
                matrix[i][j] = -100;
                dfs(matrix,i,j,result,path,value);
                path.pop_back();
            }
        }
    }
    int index = 0;
    int len = result[0].size();
    for(int i=0;i<result.size();i++){
        if(len < result[i].size()){
            index = i;
            len = result[i].size();
        }
    }
    print(result[index]);
    return;
}

int main(int argc,char* argv[]){
    /*int s = atoi(argv[1]);
    int e = atoi(argv[2]);
    int size = atoi(argv[3]);*/
   /* string whole(argv[1]);
    string wrong(argv[2]);*/

    findmax();
}