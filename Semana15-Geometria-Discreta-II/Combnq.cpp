// Geração de Combinações em ordem lexicográfica
#include<bits/stdc++.h>
using namespace std;
int	C[21], i, j, n, q, nc;

void Comb(int t,  int n, int q, int nc, int *C){
	int i, j;
    for (i=t; i<=n; i++){
        nc++;  C[nc] = i;
        if (nc == q){
            for (j=1; j<=q; j++)
				cout<<C[j]<<" "; 
			cout<<"\n";
    	}
        else Comb(i+1, n, q, nc, C);
        nc--;
    }
}

int main(){
    n =9;  q = 5;
    Comb(1, 9, 5, 0, C);
	return 0;
}
