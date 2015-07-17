#include "basic.h"

/*
mingo game
*/

inline bool check_mingo(const vector<vector<int>> &matrix,int a,int b){
	for(int i=0;i<matrix.size();i++)
		if(matrix[i][b] == 0) return false;
	for(int i=0;i<matrix[0].size();i++)
		if(matrix[a][i] == 0) return false;

	int i,j;
	i = a;j = b;
	while(i >= 0 && j>=0){
		if(matrix[i--][j--] == 0) return false;
	}
	i = a;j = b;
	while(i < matrix.size() && j <= matrix[0].size()){
		if(matrix[i++][j++] == 0) return false;
	}
	i = a;j = b;
	while(i < matrix.size() && j >=0){
		if(matrix[i++][j--] == 0) return false;
	}
	i = a;j = b;
	while(i >=0 && j <= matrix[0].size()){
		if(matrix[i--][j++] == 0) return false;
	}
	return true;
}

void mingo(){
	vector<vector<int>> matrix(10,vector<int>(10,0));
	print(matrix);
	int i = 0;
	while(i<1000){
		int x = rand()%10;
		int y = rand()%10;
		matrix[x][y] = rand()%1000;
		if(check_mingo(matrix,x,y))
			print(matrix);
		i++;
		//print(matrix);
	}
}

int main(int argc,char* argv[]){
    /*int s = atoi(argv[1]);
    int e = atoi(argv[2]);
    int size = atoi(argv[3]);*/
   /* string whole(argv[1]);
    string wrong(argv[2]);*/


    mingo();
}