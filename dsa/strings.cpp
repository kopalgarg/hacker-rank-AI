#include <iostream>
#include <string>
using namespace std;

int main() {
	string a;
    string b;
    cin >> a;
    cin >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a + b << endl;
    cout << b[0];

    for( int i = 1 ; i < a.size() ; i ++ ){
        cout << a[i];
    }
    cout << " ";

    cout << a[0];
    for( int i = 1 ; i < b.size() ; i ++ ){
        cout << b[i];
    }
    cout << endl;

    return 0;
}
