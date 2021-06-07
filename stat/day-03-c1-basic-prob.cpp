#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

int dice(int outcomeOne, int outcomeTwo){
    assert(outcomeOne > 0 && outcomeTwo > 0);
    
    if (outcomeOne < outcomeTwo) swap(outcomeOne, outcomeTwo);
    if (outcomeOne % outcomeTwo == 0) return outcomeTwo;

    return dice(outcomeTwo, outcomeOne % outcomeTwo);
}

int main(){

    int total = 6 * 6;
    int count = 0;

    for (i = 1; i <=6; i++)
        for (j = 1; i <= 6; j++)
            if (i + j <=9)
                count +=1;
    out << dice(total, count);

}