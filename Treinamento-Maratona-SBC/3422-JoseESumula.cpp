#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, O;
    string T;
    cin >> N;
    while(N > 0){
        cin >> O >> T;
        int resultado;

        if(T == "1T"){
            if(O <= 45){
                cout << O << "\n";
            } else{
                resultado = O-45;
                cout << 45 << "+" << resultado << "\n";
            }
        } else{
            if(O <= 45){
                resultado = 45+O;
                cout << resultado << "\n";
            } else{
                resultado = O-45;
                cout << 90 << "+" << resultado << "\n";
            }
        }

        N -= 1;
    }
    
    return 0;
}
