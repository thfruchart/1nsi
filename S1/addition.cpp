#include <iostream>

using namespace std;


int main () // fonction principale
{ // INITIALISATION de x 
     short x = 32760;
	
	int n, i;
	cout << "Entrer n" << endl;
	cin >> n;
	cout << endl;
	cout << "x est de type short" << endl;		
	for (i=0 ; i<n ; i++ )
		{x = x+1;
		cout << x << endl;
		}
    return 0;
}
