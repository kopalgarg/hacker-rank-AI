#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	vector<int> v;
    stringstream ss(str);
    int tmp;
    char x;
    while (ss >> tmp){
        v.push_back(tmp);
        ss >> x;
    }
    return v;
}


int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}
