#include <iostream>

using namespace std ;

int main () {

	int x ;
	cout << "Please Enter the integer that you want to reverse: ";
	cin >> x ;
	bool negative = false;
	if (x < 0 ){
		x = -x;
		negative = true;
	}

	int reversed = 0 ;

	do {

		reversed = reversed *10 + x %10;
		x /= 10;

	}
	while(x > 0);

	if (negative){
		reversed = -reversed;

	}
	cout << "Reveresed INteger : " << reversed;
}
