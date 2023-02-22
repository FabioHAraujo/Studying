#include <iomanip>
#include "pessoa.cpp"

using namespace std;

int main () {
    pessoa heroi;
    int idade, forca, resist;
    cin >> idade >> forca >> resist;
    heroi.setIdade(idade);
    cout << heroi.getInfo();
}