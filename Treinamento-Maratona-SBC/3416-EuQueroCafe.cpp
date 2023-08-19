#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, L, D;
    cin >> N >> L >> D;
    float novoD = D/1000.0; // convertendo mililitro para litro
    float litrosConsumidosPorAula = novoD * N;
    if(litrosConsumidosPorAula <= L){
        cout << L << '\n';
    } else{
        cout << ceil(litrosConsumidosPorAula/L)*L << '\n';
    }
        
    return 0;
}
