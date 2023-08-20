#include <bits/stdc++.h>
using namespace std;

vector<long long unsigned int> criaVetor(){
    vector<long long unsigned int> cartas(500000000);
    cartas[0] = 0;
    long long unsigned int nivel = 0;
    for (int i = 1; i < cartas.size(); i++){
            nivel += (3 * i) - 1;
            cartas[i] = nivel;
            //cout << nivel << '\n';
            //cout << "-----------------" << '\n';
    }
    //cout << cartas[499999999] << '\n';
    return cartas;
}

int main() {
    int T, N;
    long long unsigned int C;
    cin >> T;
    vector<long long unsigned int> cartas = criaVetor();
    while(T > 0){
        cin >> C;
        
        if(C <= 1000000000){
            long long unsigned int nivel = 0;
            for (int i = 1; i < 1000000; i++){
                nivel += (3 * i) - 1;
                if(nivel > C){
                    N = i-1;
                    cout << nivel << "\n";
                    cout << N << '\n';
                    break;
                }else if (nivel == C){
                    N = i;
                    cout << nivel << "\n";
                    cout << N << "\n";
                    break;
                }
            }
        }else{}
        

        T -= 1;
    }
    return 0;
}