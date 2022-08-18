#include <iostream>
#include <tchar.h>

int main ()
{
        _tsetlocale(LC_ALL, _T("portuguese"));
        int NumVidas = 5;
        int Score = 1350;
        std::cout << "*******************" << std::endl;
        std::cout << "Vidas Jogador: " << NumVidas << std::endl;
        std::cout << "Pontuação: " << Score << std::endl;
        std::cout << "Endereço que NumVidas Ocupa na Memória RAM: " << &NumVidas << "\n";
        std::cout << "Endereço que NumVidas Ocupa na Memória RAM: " << &Score<< "\n";
        std::cout << "*******************" << std::endl;
        system ("pause");
}