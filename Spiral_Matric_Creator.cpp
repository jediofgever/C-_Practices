#include <iostream>

using namespace std;

int main () {
	int n ;
	cout << "Please Enter the Array size: ";
	cin >> n ;
	int k =0,  l =0 ;
	int last_row = (n-1), last_column = (n-1);
	int D_Array[n][n];

	int  i ;
	int counter = 1;


		while ( k <= (n-1) && l <=(n-1)){

			for (i = l ; i <= last_column; ++i){
				D_Array[k][i] = counter;
				counter++;
			}
			k++;
			for (i = k ; i <= last_row ; ++i){
				D_Array[i][last_column] = counter ;
				counter++;

			}
			last_column--;

			if (k <= last_row){

				for (i = last_column; i>= l; --i){
					D_Array[last_row][i] = counter;
					counter++;

					}
				last_row--;
			}

			if ( l <= last_column){
				for (i = last_row; i >= k; --i){

					D_Array[i][l] = counter;
					counter++;
				}
				l++;
			}

		}

		int width = n, height = n;

		    for (int i = 0; i < height; ++i)
		    {
		        for (int j = 0; j < width; ++j)
		        {
		            std::cout << D_Array[i][j] << ' ';
		        }
		        std::cout << std::endl;
		    }
	    return 0 ;

}








