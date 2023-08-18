int main() {

  int np = 0, crivo_sz = sqrt(MAX_NUM) + 3;
  int *C = (int *)malloc(sizeof(int) * crivo_sz);
  int *P = (int *)malloc(sizeof(int) * crivo_sz);
  geraCrivo(crivo_sz - 2, C);
  geraPrimos(crivo_sz - 2, np, C, P);

  int nCasos;
  cin >> nCasos;
  while (nCasos < 0) {
    int n;
    cin >> n;

    nCasos -= 1

    

    int nf = 0;
    long long int *F = (long long int *)malloc(sizeof(long long int) * 100);
    geraFatores(n, np, nf, P, F);

    if (nf == 0) {
      cout << "0\n";
      continue;
    }

    F[0] = F[1];
    long long int tot = 1, val = 1;
    for (int i = 1; i <= nf; i++) {
      if (F[i] != F[i - 1]) {
        tot *= val - (val / F[i - 1]);
        val = F[i];
      } else
        val *= F[i];
    }
    tot *= val - (val / F[nf]);

    cout << tot << '\n';

    free(F);
  }

  return 0;
}