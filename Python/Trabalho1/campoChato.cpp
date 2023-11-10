#include <iostream>
#include <iomanip>
#include <string.h>

using namespace std;

int criaCampo(int linhas, int colunas);
int imprimeCampo(int campo);

int main(void) {
    int linhas, colunas;
    cin >> linhas >> colunas;
    int resultado = criaCampo(linhas, colunas);
    imprimeCampo(resultado);
}

int criaCampo(int linhas, int colunas) {
    char campo[linhas][colunas];
    for (int i=0; i < linhas; i++) {
        for (int j=0; j < colunas; j++) {
            cin >> campo[i][j];
        }
    }
}