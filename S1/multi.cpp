#include <iostream>
using namespace std;
int main () // fonction principale
{ // INITIALISATION de x 
    
    int x = 1;
    //short x = 1;
    //long x = 1;

	int n, i;
	cout << "Entrer n" << endl;
	cin >> n;
	cout << endl;
	cout << "calcul des puissances de 2" << endl;
		
	for (i=0 ; i<n ; i++ )
		{x = x*2;
		cout << x << endl;
		}
    return 0;
}
