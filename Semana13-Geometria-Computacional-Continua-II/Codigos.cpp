//Primitivas geométricas para retas, triangulos e circulos
#include<bits/stdc++.h>
using namespace std;

#define PI acos(-1)
const double QZERO = 0.000000001;

struct ponto { double x, y;};
struct reta { double a,b,c; };
struct circulo { ponto centro; double raio; };
struct duasretas{ reta r1,r2; };
struct doispontos { ponto p1,p2; };
struct boolponto{ bool ret; ponto p; };

int opcao;

double DistPontos(ponto p1,ponto p2){
    return (sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y)));
}

double AnguloPontoOrigem(ponto p1){
    double ang;
    if (fabs(p1.x)<QZERO){
        if (fabs(p1.y)< QZERO) ang = 0;
        else if (p1.y < 0)     ang = 3*PI/2;
        else                   ang = PI/2;
    }    
    else{
        ang = atan(p1.y/p1.x);
        if (p1.x < 0)       ang = ang + PI;
        else if (p1.y < 0)  ang = ang + 2*PI;
    }
    return ang;
}

bool PontoInteriorCirculo(ponto p1, circulo c){
    double d;
    d=DistPontos(p1,c.centro);
    if((d<c.raio) || (fabs(d-c.raio)<=QZERO)) return true;
    else return false;
}

bool Paralelas(reta r1, reta r2){
    return ((fabs(r1.a-r2.a)<=QZERO) && (fabs(r1.b-r2.b)<=QZERO));
}

bool MesmaReta(reta r1,reta r2){
    return (Paralelas(r1,r2) && (abs(r1.c-r2.c)<=QZERO));
}

boolponto PontoIntersecao(reta r1,reta r2){
    boolponto bp;
    bp.ret = true;
    if (Paralelas(r1,r2) || MesmaReta(r1,r2)) bp.ret = false;
    else{
        bp.p.x = (r2.b*r1.c-r1.b*r2.c)/(r2.a*r1.b-r1.a*r2.b);
        if (fabs(r1.b)>QZERO)
            bp.p.y = -(r1.a*bp.p.x + r1.c)/r1.b;
        else
            bp.p.y = -(r2.a*bp.p.x + r2.c)/r2.b;
        if (fabs(bp.p.x) < QZERO) bp.p.x = 0;   // Para evitar -0.00
        if (fabs(bp.p.y) < QZERO) bp.p.y = 0;   // Para evitar -0.00   
    }
    return bp;
}

reta PontosParaReta(ponto p1,ponto p2){
    reta r;
    if (p1.x==p2.x){ r.a=1; r.b =0; r.c=-p1.x;}
    else{ r.b=1; r.a=-(p1.y-p2.y)/(p1.x-p2.x);
          r.c=-(r.a*p1.x)-(r.b*p1.y);
    }
    return r;
}

reta PontoTangenteParaReta(ponto p, double tang){
    reta r;
    r.a=-tang;  r.b=1;  r.c=-(r.a*p.x + r.b*p.y);
    return r;
}

reta RetaParalela(ponto p1, reta r1){
    reta r2;
    r2.a = r1.a;  r2.b = r1.b;  r2.c = -(r1.a*p1.x + r1.b*p1.y);
    return r2;
}

reta RetaPerpendicular(ponto p1, reta r1){
    ponto p2; reta r2;
    if (fabs(r1.b)<= QZERO){
        r2.a = 0;  r2.b = 1;  r2.c = -p1.y;
    }
    else if (fabs(r1.a)<= QZERO){
        r2.a = 1;  r2.b = 0;  r2.c = -p1.x;
    }
    else r2 = PontoTangenteParaReta(p1,1/r1.a);
    return r2;
}

ponto PontoMaisProximo(ponto p1, reta r1){
    ponto p2;  boolponto bp;
    reta r2;
    if (fabs(r1.b)<= QZERO){
        p2.x = -r1.c;  p2.y = p1.y;
    }
    else if (fabs(r1.a)<= QZERO){
        p2.x = p1.x;  p2.y = -r1.c;
    }
    else{
        r2 = PontoTangenteParaReta(p1,1/r1.a);
        bp = PontoIntersecao(r1,r2);
        if (!bp.ret) cout<<"Erro"<<endl;
        p2 = bp.p;
    }
    return p2;
}

ponto RotacaoHoraria(ponto p, double ang/*em radianos*/){
    ponto p1;
    p1.x = p.x*cos(ang)-p.y*sin(ang);
    p1.y = p.x*sin(ang)+p.y*cos(ang);
    if (fabs(p1.x) < QZERO) p1.x = 0;   // Para evitar -0.00
    if (fabs(p1.y) < QZERO) p1.y = 0;   // Para evitar -0.00 
    return p1;
}

double AreaTriangulo(ponto p1, ponto p2,ponto p3){
	//Área não sinalizada
    return (0.5*fabs(p1.x*(p2.y-p3.y)-p2.x*(p1.y-p3.y)+p3.x*(p1.y-p2.y)));
}

double AreaTrianguloSinalizada(ponto p1, ponto p2,ponto p3){
    return (0.5*(p1.x*(p2.y-p3.y)-p2.x*(p1.y-p3.y)+p3.x*(p1.y-p2.y)));
}

duasretas Tangentes(ponto p1, circulo c){
    duasretas dr; double alfa,beta,d,b; ponto p0; circulo c1; int nrot;
    c1.raio = c.raio;  c1.centro.x = c.centro.x-p1.x; c1.centro.y = c.centro.y-p1.y;
    p0.x =0;  p0.y = 0;  nrot = 0;
	while (((c1.centro.x < 0) && (fabs(c1.centro.x) > QZERO)) ||
          ((c1.centro.y < 0) && (fabs(c1.centro.y) > QZERO))) {
        nrot++;  c1.centro = RotacaoHoraria(c1.centro, PI/2);
    }
 	d = DistPontos(p0,c1.centro);   b = sqrt(d*d-c1.raio*c1.raio);
    alfa = atan(c1.raio/b);
    if (nrot > 1) nrot = nrot -2; // Mesma tangente
	if (fabs(c1.centro.x) <= QZERO) beta = PI/2*(nrot-1);
	else                        beta = atan(c1.centro.y/c1.centro.x) -PI/2*nrot;
    if (fabs(cos(beta-alfa)) <= QZERO) {
        dr.r1.a = 1;  dr.r1.b = 0;  dr.r1.c = -p1.x;
    }
    else dr.r1 = PontoTangenteParaReta(p1,sin(beta-alfa)/cos(beta-alfa));
    if (fabs(cos(beta+alfa)) <= QZERO) {
        dr.r2.a = 1;  dr.r2.b = 0;  dr.r2.c = -p1.x;
    }
    else dr.r2 = PontoTangenteParaReta(p1,sin(beta+alfa)/cos(beta+alfa));
	return dr;
}

doispontos PontosTangencia(ponto p1, circulo c){
    duasretas dr;  doispontos dp;
    dr = Tangentes(p1,c);
    dp.p1 = PontoMaisProximo(c.centro,dr.r1);
    dp.p2 = PontoMaisProximo(c.centro,dr.r2);
    if (fabs(dp.p1.x) < QZERO) dp.p1.x = 0;   // Para evitar -0.00
    if (fabs(dp.p1.y) < QZERO) dp.p1.y = 0;   // Para evitar -0.00 
    if (fabs(dp.p2.x) < QZERO) dp.p2.x = 0;   // Para evitar -0.00
    if (fabs(dp.p2.y) < QZERO) dp.p2.y = 0;   // Para evitar -0.00    
    return dp;
}

void ExemploPontosParaReta(){
    ponto p1,p2;
    reta r;
    cout<<"Exemplo de uso de PontosParaReta"<<endl;
    cout<<"Entre com x e y de p1: "; cin>>p1.x>>p1.y;
    cout<<"Entre com x e y de p2: "; cin>>p2.x>>p2.y;
    r = PontosParaReta(p1,p2);
    cout<<"Reta: "<<r.a<<"x + "<<r.b<<"y + "<<r.c<<" = 0"<<endl<<endl;
}

void ExemploPontoTangenteParaReta(){
    ponto p;
    reta r;
    double tang;
    cout<<"Exemplo de uso de PontoTangenteParaReta"<<endl;
    cout<<"Entre com x e y de p: "; cin>>p.x>>p.y;
    cout<<"Entre com a tangente: "; cin>>tang;
    r = PontoTangenteParaReta(p,tang);
    cout<<"Reta: "<<r.a<<"x + "<<r.b<<"y + "<<r.c<<" = 0"<<endl<<endl;
}

void ExemploPontoIntersecao(){
    ponto p1,p2,p3;  boolponto bp;
    reta r1,r2;
    cout<<"Exemplo de uso de PontoIntersecao"<<endl;
    cout<<"Entre com coordenadas de p1 e p2 da reta 1: "; cin>>p1.x>>p1.y>>p2.x>>p2.y;
    r1=PontosParaReta(p1,p2);
    cout<<"Entre com coordenadas de p3 e p4 da reta 2: "; cin>>p1.x>>p1.y>>p2.x>>p2.y;
    r2= PontosParaReta(p1,p2);
    cout<<"Reta 1: "<<r1.a<<"x + "<<r1.b<<"y + "<<r1.c<<" = 0"<<endl;
    cout<<"Reta 2: "<<r2.a<<"x + "<<r2.b<<"y + "<<r2.c<<" = 0"<<endl;
    if (MesmaReta(r1,r2)) cout<<"Mesma reta"<<endl;
    else if (Paralelas(r1,r2)) cout<<"Retas Paralelas"<<endl;
    else{
        bp = PontoIntersecao(r1,r2);
        p3 = bp.p;
        cout<<"Ponto de Intersecao: "<<p3.x<<" "<<p3.y<<endl;
    }
    cout<<endl;
}

void ExemploRetaParalela(){
    ponto p1,p2;
    reta r1,r2;
    cout<<"Exemplo de uso de RetaParalela"<<endl;
    cout<<"Entre com coordenadas de p1 e p2 da reta: "; cin>>p1.x>>p1.y>>p2.x>>p2.y;
    r1= PontosParaReta(p1,p2);
    cout<<"Entre com coordenadas de p: "; cin>>p1.x>>p1.y;
    r2 = RetaParalela(p1,r1);
    cout<<"Reta 1       : "<<r1.a<<"x + "<<r1.b<<"y + "<<r1.c<<" = 0"<<endl;
    cout<<"Reta parakeka: "<<r2.a<<"x + "<<r2.b<<"y + "<<r2.c<<" = 0"<<endl<<endl;
}

void ExemploRetaPerpendicular(){
    ponto p1,p2;
    reta r1,r2;
    cout<<"Exemplo de uso de RetaPerpendicular"<<endl;
    cout<<"Entre com coordenadas de p1 e p2 da reta: "; cin>>p1.x>>p1.y>>p2.x>>p2.y;
    r1= PontosParaReta(p1,p2);
    cout<<"Entre com coordenadas de p: "; cin>>p1.x>>p1.y;
    r2 = RetaPerpendicular(p1,r1);
    cout<<"Reta 1            : "<<r1.a<<"x + "<<r1.b<<"y + "<<r1.c<<" = 0"<<endl;
    cout<<"Reta perpendicular: "<<r2.a<<"x + "<<r2.b<<"y + "<<r2.c<<" = 0"<<endl<<endl;
}

void ExemploPontoMaisProximo(){
    ponto p1,p2;
    reta r1;
    cout<<"Exemplo de uso de PontoMAisProximo"<<endl;
    cout<<"Entre com coordenadas de p1 e p2 da reta: "; cin>>p1.x>>p1.y>>p2.x>>p2.y;
    r1=PontosParaReta(p1,p2);
    cout<<"Entre com coordenadas de p1: "; cin>>p1.x>>p1.y;
    p2= PontoMaisProximo(p1,r1);
    cout<<"Reta: "<<r1.a<<"x + "<<r1.b<<"y + "<<r1.c<<" = 0"<<endl;
    cout<<"O ponto mais proximo a: "<<p1.x<<" "<<p1.y<<" eh: "<<p2.x<<" "<<p2.y<<endl<<endl;
}

void ExemploRotacaoHoraria(){
    ponto Tri1[3],Tri2[3];
    int i;
    double alfa;
    char resposta;
    cout<<"Exemplo de uso de RotacaoHoraria"<<endl;
    cout<<"Entre com x e y de trÃªs pontos do triÃ¢ngulo: ";
    for(i = 0; i<3; i++) cin>>Tri1[i].x>>Tri1[i].y;
    cout<<"Quer informar o angulo em radianos? S ou N: "; cin>>resposta;
    if (resposta == 's' || resposta == 'S'){
        cout<<"Entre com o Ã¢ngulo de rotacao(radianos): "; cin>>alfa;
    }
    else{
      cout<<"Entre com o Ã¢ngulo de rotacao(graus): "; cin>>alfa;
      alfa = PI*alfa/180;
    }
    for(i=0; i<3; i++)  Tri2[i] = RotacaoHoraria(Tri1[i],-alfa);
    cout<<"Antes: ";
    for(i=0; i<3; i++) cout<<Tri1[i].x<<" "<<Tri1[i].y<<" "; cout<<endl;
    cout<<"Depois: ";
    for(i=0; i<3; i++) cout<<Tri2[i].x<<" "<<Tri2[i].y<<" "; cout<<endl;
    cout<<endl;
}

void ExemploAreaTriangulo(){
    ponto p1,p2,p3;
    cout<<"Exemplo de uso de AreaTriangulo"<<endl;
    cout<<"Entre com x e y de trÃªs pontos do triÃ¢ngulo: ";
    cin>>p1.x>>p1.y>>p2.x>>p2.y>>p3.x>>p3.y;
    cout<<"Area do triÃ¢ngulo: "<<AreaTriangulo(p1,p2,p3)<<endl<<endl;
}

void ExemploPontoInteriorCirculo(){
    ponto p1;
    circulo c;
    cout<<"Exemplo de uso de PontoInteriorCirculo"<<endl;
    cout<<"Entre com o centro (x e y) e o raio do cÃ­rculo: ";
    cin>>c.centro.x>>c.centro.y>>c.raio;
    cout<<"Entre com o ponto de teste(x e y): ";
    cin>>p1.x>>p1.y;
    if (PontoInteriorCirculo(p1,c)) cout<<"Ponto interior ao circulo"<<endl;
    else                            cout<<"Ponto exterior ao cÃ­rculo"<<endl;
    cout<<endl;
}

void ExemploTangentes() {
    ponto p1; circulo c;  duasretas dr;
    cout<<"Exemplo de uso de Tangentes"<<endl;
    cout<<"Entre com o centro (x e y) e o raio do círculo: ";
    cin>>c.centro.x>>c.centro.y>>c.raio;
    cout<<"Entre com o ponto de teste(x e y): ";
    cin>>p1.x>>p1.y;
    if (PontoInteriorCirculo(p1,c)) cout<<"Ponto interior ao circulo"<<endl;
    else {
        dr = Tangentes(p1,c);
        cout<<"Primeira tangente: "<<dr.r1.a<<"x + "<<dr.r1.b<<"y + "<<dr.r1.c<<" = 0"<<endl;
        cout<<"Segunda  tangente: "<<dr.r2.a<<"x + "<<dr.r2.b<<"y + "<<dr.r2.c<<" = 0"<<endl;
    }
    cout<<endl;
}

void ExemploPontosTangencia(){
    ponto p1; circulo c; doispontos dp;
    cout<<"Exemplo de uso de PontosTangencia"<<endl;
    cout<<"Entre com o centro (x e y) e o raio do círculo: ";
    cin>>c.centro.x>>c.centro.y>>c.raio;
    cout<<"Entre com o ponto de teste(x e y): ";
    cin>>p1.x>>p1.y;
    if (PontoInteriorCirculo(p1,c)) cout<<"Ponto interior ao circulo"<<endl;
    else{
        dp = PontosTangencia(p1, c);
        cout<<"Primeiro ponto de tangencia: "<<dp.p1.x<<" "<<dp.p1.y;
        cout<<"Segundo  ponto de tangencia: "<<dp.p2.x<<" "<<dp.p2.y;
    }
    cout<<endl;
}

void ExemploAnguloPontoOrigem(){
    ponto p1; double ang;
    cout<<"Exemplo de uso de AnguloPontoOrigem"<<endl;
    cout<<"Entre com o ponto de teste(x e y): ";
    cin>>p1.x>>p1.y;  ang = AnguloPontoOrigem(p1);
    cout<<"Angulo em radianos: " << ang <<" Angulo em graus: " << 180*ang/PI <<endl;
    cout<<endl;
}

int main(){
    cout.setf(ios_base::fixed); //a parte fracionÃ¡ria do nÃºmero em ponto flutuante serÃ¡ impressa com exatamente a quantidade de digitos
    cout.precision(2);		//especificados pela precisÃ£o, nesse caso com 2 casas decimas.
    cout<<"Opcao: "; cin>>opcao;
    while(opcao > 0){
        switch(opcao){
            case 1: ExemploPontosParaReta();
                    break;
            case 2: ExemploPontoTangenteParaReta();
                    break;
            case 3: ExemploPontoIntersecao();
                    break;
            case 4: ExemploRetaParalela();
                    break;
            case 5: ExemploRetaPerpendicular();
                    break;
            case 6: ExemploPontoMaisProximo();
                    break;
            case 7: ExemploRotacaoHoraria();
                    break;
            case 8: ExemploAreaTriangulo();
                    break;
            case 9: ExemploPontoInteriorCirculo();
                    break;                    
            case 10: ExemploTangentes();
                    break;
            case 11: ExemploPontosTangencia();
                    break; 
            case 12: ExemploAnguloPontoOrigem();
                    break;
        }
        cout<<"Opcao: "; cin>>opcao;
    }
}