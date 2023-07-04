//Primitivas de Geometria Computacional
// CONVENÇÕES:
// Os pontos lidos são colocados em um vetor de pontos com a numeração a partir de 0.
// Em alguns casos, para poligonos, é feito pol[n] = pol[0], mas o número de pontos
//             continua sendo n.
// Área Polígono: retorna a área SINALIZADA. Tem que usar fabs para obter a área real
// Convex Hull: está retornando o tamanho da convex hull de duas formas: como parâmetro
//              e no retorno da função.
// PontoInteriorPoligonoConvexo: retorna 1 se o ponto está sobre um dos lados.
// PontoInterior: retorna 1 se o ponto está sobre um dos lados.
// OrdenaCoordenada: ordena os pontos pela coordenada x. Para pontos com mesmox, ordena por y.
// Programas URI usados para teste: 2581, 1560, 1971, 1982, 2541
#include<iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<algorithm>
using namespace std;
typedef struct {int x, y;}Ponto;
typedef struct {Ponto p, q;}Segmento;
Ponto pol[100000], ch[100000]; //vetores globais


int SentidoPercurso(Ponto p1, Ponto p2, Ponto p3)
{  long long a, b, c, d;
   a= p2.x - p1.x;
   b= p3.y - p1.y;
   c=p3.x - p1.x;
   d=p2.y - p1.y;
   a = a*b-c*d;
   if (a > 0) return 1;
   else if (a < 0) return -1;
   else return 0;
}
int Intercepta(Segmento s1, Segmento s2)
{  if ((max(s1.p.x,s1.q.x)>=min(s2.p.x,s2.q.x))&&
       (max(s2.p.x,s2.q.x)>=min(s1.p.x,s1.q.x))&&
       (max(s1.p.y,s1.q.y)>=min(s2.p.y,s2.q.y))&&
       (max(s2.p.y,s2.q.y)>=min(s1.p.y,s1.q.y))&&
       (SentidoPercurso(s1.p,s1.q,s2.p)*SentidoPercurso(s1.p,s1.q,s2.q)<=0)&&
       (SentidoPercurso(s2.p,s2.q,s1.p)*SentidoPercurso(s2.p,s2.q,s1.q)<=0))
       return 1;
    else return 0;     
}

double AreaPoligono(Ponto *pol, int n)
{  long long c;  int i;
   pol[n] = pol[0];
   c = 0;  for (i=0; i<n; i++) c= c + pol[i].x*pol[i+1].y-pol[i+1].x*pol[i].y;
   return c/2.0;
}

void Quicksort(Ponto *pol, int e, int d)
// O ponto 0 fica fixo na ordenação, pois tem o menor x
{  int i,j,k;  Ponto t,r;  long long d0, d1, d2;
   if (d > e)
   {  i=e;  j=d;  t=pol[(e+d)/2];
      d1= pol[0].x-t.x;  d2= pol[0].y-t.y;  d0=d1*d1+d2*d2;
      while(i<=j)
      {  while(1)
         {  k=SentidoPercurso(pol[0],pol[i],t);
            if (k==1) i++;
            else if (k==0)
            {  d1= pol[0].x-pol[i].x;  d2= pol[0].y-pol[i].y;  d1= d1*d1+d2*d2;
               if (d1 < d0) i++;
               else break;
            }   
            else break;
         }
         while(1)
         {  k=SentidoPercurso(pol[0],t,pol[j]);
            if (k==1) j--;
            else if (k==0)
            {  d1= pol[0].x-pol[j].x;  d2= pol[0].y-pol[j].y;  d1= d1*d1+d2*d2;
               if (d0 < d1) j--;
               else break;
            }
            else break;
         }  
         if (i<=j) {r=pol[i];  pol[i]=pol[j];  pol[j]=r;  i++; j--;}
      }
      Quicksort(pol, e,j);  Quicksort(pol, i,d);
   }
}          
void OrdenaPontosy(Ponto *pol, int tp)
/*   Ordena pontos por ângulo, escolhendo como referência o ponto mais embaixo e mais
   à esquerda. */
{  int i,m;  Ponto p;
   m=0;
   for (i=1;i<tp;i++) 
      if ((pol[i].y < pol[m].y)||(pol[i].y==pol[m].y)&&(pol[i].x<pol[m].x)) m=i;
   p=pol[0];  pol[0]=pol[m];  pol[m]=p;
   Quicksort(pol, 1,tp-1);
}    
void OrdenaPontosx(Ponto *pol, int tp)
/* Ordena pontos por ângulo, escolhendo como referência o ponto mais à esquerda e mais
   embaixo. */
{  int i,m;  Ponto p;
   m=0;
   for (i=1;i<tp;i++) 
      if ((pol[i].x < pol[m].x)||(pol[i].x==pol[m].x)&&(pol[i].y<pol[m].y)) m=i;
   p=pol[0];  pol[0]=pol[m];  pol[m]=p;
   Quicksort(pol, 1,tp-1);
}

void CaminhoFechado(Ponto *pol, int tp)
/* Ordena pontos e, ao final da ordenação, se houver pontos colineares com
   o ponto inicial, no final do vetor, a ordem dos pontos colineares é invertida. */
{  int i,m;  Ponto p;
   OrdenaPontosx(pol, tp);
   i = tp-1;  while ((i>0)&&(SentidoPercurso(pol[0],pol[i-1],pol[i])==0)) i--;
   for (m=i; m<(i+tp)/2;m++) {p=pol[m]; pol[m]=pol[tp-1-m+i]; pol[tp-1-m+i]=p;}
}

int ConvexHull(Ponto *pol, int tp, Ponto *ch, int &tc)
{   int i,j,topo;
    OrdenaPontosy(pol, tp);
    /*Repete o ponto inicial no final*/
    ch[0]= pol[0]; pol[tp]= pol[0];
    j= 1;
    /* Elimina pontos iniciais colineares */
    while (SentidoPercurso(ch[0],pol[j],pol[j+1])==0) j++;
    ch[1]= pol[j];  ch[2]= pol[j+1];
    topo= 2;
    for (i= j+2; i<= tp; i++)
    {   while (SentidoPercurso(ch[topo-1], ch[topo], pol[i]) <= 0) topo--;
        topo++;  ch[topo]= pol[i];
    }
    tc = topo;
    return (topo);
}

int PoligonoConvexo(Ponto *pol, int n){
	int s, i; 
	s = SentidoPercurso(pol[n-2], pol[n-1], pol[0]);
	if (s != SentidoPercurso(pol[n-1], pol[0], pol[1]))
		return 0;
    for (i=0; i<n-2; i++) if (s != SentidoPercurso(pol[i], pol[i+1], pol[i+2]))
		return 0;
	return 1;
}

int PontoNoSegmento(Ponto p0, Ponto p1, Ponto p2){
    return SentidoPercurso(p0, p1, p2) == 0 &&
           p0.x >= min(p1.x, p2.x) && p0.x <= max(p1.x, p2.x) &&
           p0.y >= min(p1.y, p2.y) && p0.y <= max(p1.y, p2.y);
}

int PontoInteriorPoligonoConvexo(Ponto *pol, int n, Ponto q){
	int t, t1, i; 
	pol[n] = pol[0];
	t = SentidoPercurso(q, pol[n-1], pol[0]);
	if (t==0)
	    return PontoNoSegmento(q, pol[n-1], pol[0]);
    for (i=1; i<=n-1; i++){
        t1 = SentidoPercurso(q, pol[i-1], pol[i]);
		if (t1==0)
	    	return PontoNoSegmento(q, pol[i-1], pol[i]);        
		if (t != t1)
			return 0;
	}
	return 1;
}

int PontoInterior(Ponto *pol, int n, Ponto q){
	int i, maxx = pol[0].x, cont; Segmento s1, s2;
	pol[n] = pol[0];
	for (i=1; i<=n; i++){
		if (PontoNoSegmento(q, pol[i-1], pol[i]))
			return 1;
		if (pol[i].x > maxx) maxx = pol[i].x;
	}
	s2.p = q;  s2.q.x = maxx+1;  s2.q.y = q.y;
	cont=0;
	for (i=1; i<=n; i++){
		s1.p = pol[i-1];  s1.q = pol[i];  
		if ((pol[i].y > q.y && pol[i-1].y <= q.y || pol[i-1].y > q.y && pol[i].y <= q.y)
			 && (Intercepta(s1, s2)))
			cont++;
	}	
	return cont%2;
}

bool comparax(Ponto p1, Ponto p2){
    if (p1.x == p2.x)
    	return p1.y < p2.y;
    return p1.x < p2.x;
}

void OrdenaPontosPorx(Ponto *pol, int np){
	sort(pol, pol+np, comparax);
}

void ExemploSentidoPercurso(){
    Ponto p1,p2,p3;  int j;
    cout<<"Exemplo de uso de SentidoPercurso"<<endl;
    cout<< "Entre com as coordenadas (x,y) de p1, p2 e p3: ";
    cin>>p1.x >>p1.y >>p2.x >>p2.y >>p3.x >>p3.y;
    j= SentidoPercurso(p1,p2,p3);
    if (j==1)       cout<<"Antihorario"<<endl;
    else if (j==-1) cout<<"Horario" <<endl;
    else            cout<<"Pontos colineares"<<endl;
    cout<<endl;
}

void ExemploIntersecaoSegmentos(){
    Segmento s1,s2;
    cout<<"Exemplo de uso de Intercepta" <<endl;
    cout<<"Entre com o segmento 1 (p1 e p2): ";
    cin>> s1.p.x >> s1.p.y >> s1.q.x >> s1.q.y;
    cout<< "Entre com o segmento 2 (p3 e p4): ";
    cin>> s2.p.x >> s2.p.y >> s2.q.x >> s2.q.y;
    if (Intercepta(s1,s2)==1) cout<< "Interceptam" <<endl;
    else cout<< "Nao interceptam" <<endl;
    cout<<endl;
}

void ExemploAreaPoligono(){
    int i, np;
    cout<< "Exemplo de uso de AreaPoligono" <<endl;
    cout<< "Entre com o número de vertices: ";  cin>> np;
    for (i=0; i<np; i++) {
        cout<< "Entre com o ponto " <<i+1 <<" : ";
        cin>> pol[i].x >>pol[i].y;
    }
    pol[np] = pol[0];
    cout<<"Area do poligono = " <<AreaPoligono(pol, np) <<endl;
    cout<<endl;
}

void ExemploCaminhoFechado(){
    int i, np;
    cout<< "Exemplo de uso de CaminhoFechado" <<endl;
    cout<< "Entre com o número de pontos: ";  cin>> np;
    for (i=0; i<np; i++) {
        cout<< "Entre com o ponto " <<i+1 <<" : ";
        cin>> pol[i].x >>pol[i].y;
    }
    CaminhoFechado(pol, np);
    cout<<"Caminho fechado:";
    for (i=0; i<np; i++) cout<< pol[i].x <<" " <<pol[i].y <<" ";
    cout<<endl<<endl;
}

void ExemploContornoConvexo(){
    int i, np, nv;
    cout<< "Exemplo de uso de ConvexHull" <<endl;
    cout<< "Entre com o número de pontos: ";  cin>> np;
    for (i=0; i<np; i++) {
        cout<< "Entre com o ponto " <<i+1 << " : ";
        cin>> pol[i].x >>pol[i].y;
    }
    nv = ConvexHull(pol, np, ch, nv);
    cout<<"Contorno Convexo com " <<nv-1 <<" pontos:";
    for (i=0; i<=nv; i++) cout<< ch[i].x <<" " <<ch[i].y <<" ";
    cout<<endl<<endl;    
}

void ExemploPoligonoConvexo(){
    int i, np, nv;
    cout<< "Exemplo de teste de Poligono Convexo" <<endl;
    cout<< "Entre com o número de pontos do poligono: ";  cin>> np;
    for (i=0; i<np; i++) {
        cout<< "Entre com o ponto " <<i+1 << " : ";
        cin>> pol[i].x >>pol[i].y;
    }
    if (PoligonoConvexo(pol, np)) cout<<"O poligono eh convexo"<<endl;
    else cout<<"O poligono nao eh convexo"<<endl;  
}

void ExemploPontoInteriorPoligonoConvexo(){
    int i, np, nv;  Ponto q;
    cout<< "Exemplo de teste de Ponto Interior a Poligono Convexo" <<endl;
    cout<< "Entre com o número de pontos do poligono: ";  cin>> np;
    for (i=0; i<np; i++) {
        cout<< "Entre com o ponto " <<i+1 << " : ";
        cin>> pol[i].x >>pol[i].y;
    }
    if (PoligonoConvexo(pol, np)){
    	cout<< "Entre com o ponto a ser testado: ";
     	cin>> q.x >>q.y;
    	if (PontoInteriorPoligonoConvexo(pol, np, q)) cout<<"O ponto eh interior ao poligono convexo"<<endl;
    	else cout<<"O ponto nao eh interior ao poligono convexo"<<endl; 
	}
    else cout<<"O poligono nao eh convexo. Nao sera feito o teste"<<endl;  
}

void ExemploPontoInterior(){
    int i, np, nv;  Ponto q;
    cout<< "Exemplo de teste de Ponto Interior" <<endl;
    cout<< "Entre com o número de pontos do poligono: ";  cin>> np;
    for (i=0; i<np; i++) {
        cout<< "Entre com o ponto " <<i+1 << " : ";
        cin>> pol[i].x >>pol[i].y;
    }
    cout<< "Entre com o ponto a ser testado: ";
     cin>> q.x >>q.y;
    if (PontoInterior(pol, np, q)) cout<<"O ponto eh interior ao poligono"<<endl;
    else cout<<"O ponto nao eh interior ao poligono"<<endl;  
}
void ExemploOrdenaCoordenada(){
    //Este programa ordena um vetor de pontos pela coordenada x e, quando essa coordenada
    // é constante, pela coordenada y
    int i, np, nv;  Ponto q;
    cout<< "Exemplo de teste de Ordenação de Coordenada" <<endl;
    cout<< "Entre com o número de pontos: ";  cin>> np;
    for (i=0; i<np; i++) {
        cout<< "Entre com o ponto " <<i+1 << " : ";
        cin>> pol[i].x >>pol[i].y;
    }
    cout<<endl<<"Situacao inicial:"<<endl;
    for (i=0; i<np; i++) cout<<pol[i].x<<" "<<pol[i].y<<" ";
    OrdenaPontosPorx(pol, np);
	//sort(pol, pol+np, comparax);
    cout<<endl<<"Situacao final:"<<endl;
    for (i=0; i<np; i++) cout<<pol[i].x<<" "<<pol[i].y<<" ";    
}

int main()
{   int opcao;
    cout<<fixed;             //a parte fracionÃ¡ria do nÃºmero em ponto flutuante serÃ¡ impressa com exatamente a quantidade de digitos
    cout.precision(2);		//especificados pela precisÃ£o, nesse caso com 2 casas decimas.
    cout<<"Opcao: "; cin>>opcao;
    while(opcao > 0){
        switch(opcao){
            case 1: ExemploSentidoPercurso();
                    break;
            case 2: ExemploIntersecaoSegmentos();
                    break;
            case 3: ExemploAreaPoligono();
                    break;
            case 4: ExemploCaminhoFechado();
                    break;
            case 5: ExemploContornoConvexo();
                    break;
            case 6: ExemploPoligonoConvexo();
                    break;   
            case 7: ExemploPontoInteriorPoligonoConvexo();
                    break; 					                 
            case 8: ExemploPontoInterior();
                    break;   
            case 9: ExemploOrdenaCoordenada();
                    break;                       
        }
        cout<<"Opcao: "; cin>>opcao;
    }   
   return 0;
}    